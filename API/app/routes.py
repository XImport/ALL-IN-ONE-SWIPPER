from flask import jsonify, request
from app import app
import os
import pandas as pd
from datetime import datetime


def get_files_in_directory(directory_path):
    """
    List all files in the specified directory recursively.

    Args:
        directory_path (str): Path of the directory to search in.

    Returns:
        list: List of file paths.
    """
    try:
        all_files = []
        for root, _, files in os.walk(directory_path):
            for file in files:
                all_files.append(os.path.join(root, file))
        return all_files
    except FileNotFoundError:
        return None
    except Exception as e:
        return str(e)


@app.route("/API/TESTING")
def hello_world():
    return jsonify({"Message": "Hello API"})


@app.route("/API/V1/BalanceSheet", methods=["POST"])
def balance_sheet():
    try:
        # Retrieve dates from the request body
        debut_date = request.json.get("DébutDate")
        fin_date = request.json.get("FinDate")

        if not debut_date or not fin_date:
            return jsonify({"Message": "DébutDate and FinDate are required."}), 400

        print("Dates received:", debut_date, fin_date)

        # Path to the source directory
        source_path = "./app/Source"
        files = get_files_in_directory(source_path)

        if not files:
            return (
                jsonify({"Message": f"No files found in the directory {source_path}."}),
                404,
            )

        # Load both sheets from the Excel file
        convert_data_json = pd.read_excel(files[0], sheet_name="VENTES")
        convert_data_json2 = pd.read_excel(files[0], sheet_name="RECOUVREMENT")

        # Convert "Date" column to datetime for both dataframes
        convert_data_json["Date"] = pd.to_datetime(
            convert_data_json["Date"], format="%d/%m/%Y", errors="coerce"
        )
        convert_data_json2["Date de Paiement"] = pd.to_datetime(
            convert_data_json2["Date de Paiement"], format="%d/%m/%Y", errors="coerce"
        )

        # Convert input dates to datetime objects
        try:
            debut_date = pd.to_datetime(debut_date, format="%d/%m/%Y")
            fin_date = pd.to_datetime(fin_date, format="%d/%m/%Y")
        except ValueError:
            return (
                jsonify(
                    {"Message": "Invalid date format. Please use DD/MM/YYYY format."}
                ),
                400,
            )

        # Filter both datasets between DébutDate and FinDate
        filtered_data = convert_data_json[
            (convert_data_json["Date"].dt.date >= debut_date.date())
            & (convert_data_json["Date"].dt.date <= fin_date.date())
        ]

        filtered_data2 = convert_data_json2[
            (convert_data_json2["Date de Paiement"].dt.date >= debut_date.date())
            & (convert_data_json2["Date de Paiement"].dt.date <= fin_date.date())
        ]

        if filtered_data.empty and filtered_data2.empty:
            return (
                jsonify(
                    {
                        "Message": "No data found between the specified dates in either sheet.",
                        "Available_Dates_VENTES": convert_data_json["Date"]
                        .dt.strftime("%d/%m/%Y")
                        .unique()
                        .tolist(),
                        "Available_Dates_RECOUVREMENT": convert_data_json2[
                            "Date de Paiement"
                        ]
                        .dt.strftime("%d/%m/%Y")
                        .unique()
                        .tolist(),
                    }
                ),
                404,
            )

        # Convert dates back to string format for JSON response
        filtered_data["Date"] = filtered_data["Date"].dt.strftime("%d/%m/%Y")
        filtered_data2["Date de Paiement"] = filtered_data2[
            "Date de Paiement"
        ].dt.strftime("%d/%m/%Y")

        # Calculate metrics from filtered_data
        CABRUT = sum(filtered_data["CA BRUT"].tolist())
        CANET = sum(filtered_data["CA Net"].tolist())
        PMVGLOBAL = sum(filtered_data["CA Net"].tolist()) / sum(
            filtered_data["Qté en T"].tolist()
        )
        CANOBLES = sum(
            filtered_data[filtered_data["Type"] == "Nobles"]["CA Net"].tolist()
        )
        CAGRAVES = sum(
            filtered_data[filtered_data["Type"] == "Graves"]["CA Net"].tolist()
        )

        VOLNOBLES = sum(
            filtered_data[filtered_data["Type"] == "Nobles"]["Qté en T"].tolist()
        )
        VOLGRAVES = sum(
            filtered_data[filtered_data["Type"] == "Graves"]["Qté en T"].tolist()
        )
        VOLSTERILE = sum(
            filtered_data[filtered_data["Type"] == "Stérile"]["Qté en T"].tolist()
        )

        PMVHORSSTERILE = (CANOBLES + CAGRAVES) / (VOLNOBLES + VOLGRAVES)

        MARGETRANSPORT = sum(filtered_data["CA Transport"].tolist()) - sum(
            filtered_data["Coût de transport"].tolist()
        )
        QNTENTONNE = sum(filtered_data["Qté en T"].tolist())
        QNTENM3 = sum(filtered_data["Qté en m3"].tolist())
        MIXPRODUIT = (VOLNOBLES) / (VOLNOBLES + VOLGRAVES + VOLSTERILE) * 100
        CACAISSE = sum(
            filtered_data[filtered_data["BC"] == "EN ESPECE"]["CA BRUT"].tolist()
        )
        VOYAGESRENDULIV = filtered_data[filtered_data["Chantier"] != "DEPART"].shape[0]
        RECOUVREMENT = sum(filtered_data2["Montant Paye"].tolist())

        GRAPHVOYAGESRENDULIVDATES = (
            filtered_data[filtered_data["Chantier"] != "DEPART"]["Date"]
            .unique()
            .tolist()
        )
        GRAPHVOYAGERENDULIVREE = (
            filtered_data[filtered_data["Chantier"] != "DEPART"]
            .groupby("Date")["Ticket/BL"]
            .count()
            .tolist()
        )
        GRAPHVOYAGERENDUCOMMANDEE = (
            filtered_data[filtered_data["Chantier"] != "DEPART"]
            .groupby("Date")["Ticket/BL"]
            .count()
            .tolist()
        )
        ############################################################################################################
        GRAPHQNTENTONNEDATES = filtered_data["Date"].unique().tolist()

        filtered_data["Qté en T"] = pd.to_numeric(
            filtered_data["Qté en T"], errors="coerce"
        )
        filtered_data["Qté en m3"] = pd.to_numeric(
            filtered_data["Qté en m3"], errors="coerce"
        )

        # Group by "Date" and sum "Qté en T" and "Qté en m3" for each date
        sum_per_date = (
            filtered_data.groupby("Date")[["Qté en T", "Qté en m3"]].sum().reset_index()
        )

        # Convert the result into a list of dictionaries
        GRAPHQNTENTONNEDATES = sum_per_date.to_dict(orient="records")

        # Output the result
        # Separate the Date, Qté en T, and Qté en m3 into individual lists
        GRAPHVOLDATES = [entry["Date"] for entry in GRAPHQNTENTONNEDATES]
        GRAPHVOLQNTENT = [entry["Qté en T"] for entry in GRAPHQNTENTONNEDATES]
        GRAPHVOLQNTENM3 = [entry["Qté en m3"] for entry in GRAPHQNTENTONNEDATES]
        ################################################################################################################
        # Assuming filtered_data is already loaded and contains the required data
        GRAPHCADATES = filtered_data["Date"].unique().tolist()

        # Ensure that "CA BRUT" and "CA Net" are numeric
        filtered_data["CA BRUT"] = pd.to_numeric(
            filtered_data["CA BRUT"], errors="coerce"
        )
        filtered_data["CA Net"] = pd.to_numeric(
            filtered_data["CA Net"], errors="coerce"
        )

        # Group by "Date" and sum "CA BRUT" and "CA Net" for each date
        sum_per_date = (
            filtered_data.groupby("Date")[["CA BRUT", "CA Net"]].sum().reset_index()
        )

        # Convert the result into a list of dictionaries
        GRAPHCADATES = sum_per_date.to_dict(orient="records")

        # Separate the Date, CA BRUT, and CA Net into individual lists
        GRAPHCADATESS = [entry["Date"] for entry in GRAPHCADATES]
        GRAPHCABRUT = [entry["CA BRUT"] for entry in GRAPHCADATES]
        GRAPHCANET = [entry["CA Net"] for entry in GRAPHCADATES]

        ##################################################################################################################

        return (
            jsonify(
                {
                    "Message": "Balance Sheet",
                    "RECOUVREMENT_Data": filtered_data2.to_dict(orient="records"),
                    "VENTES_Records": len(filtered_data),
                    "RECOUVREMENT_Records": len(filtered_data2),
                    "Metrics1": {
                        "CABRUT": CABRUT,
                        "CANET": CANET,
                        "PMVGLOBAL": PMVGLOBAL,
                        "PMVHORSSTERILE": PMVHORSSTERILE,
                        "MARGETRANSPORT": MARGETRANSPORT,
                        "QNTENTONNE": QNTENTONNE,
                    },
                    "Metrics2": {
                        "MIXPRODUIT": MIXPRODUIT,
                        "CACAISSE": CACAISSE,
                        "VOYAGESRENDULIV": VOYAGESRENDULIV,
                        "RECOUVREMENTCOMMERCIALE": RECOUVREMENT,
                    },
                    "COMMANDEGRAPH": {
                        "GRAPHVOYAGESRENDULIVDATES": GRAPHVOYAGESRENDULIVDATES,
                        "GRAPHVOYAGERENDULIVREE": GRAPHVOYAGERENDULIVREE,
                        "GRAPHVOYAGERENDUCOMMANDEE": GRAPHVOYAGERENDUCOMMANDEE,
                    },
                    "VOLGRAPH": {
                        "GRAPHVOLDATES": GRAPHVOLDATES,
                        "GRAPHVOLQNTENT": GRAPHVOLQNTENT,
                        "GRAPHVOLQNTENM3": GRAPHVOLQNTENM3,
                    },
                    "CAGRAPH": {
                        "GRAPHCADATESS": GRAPHCADATESS,
                        "GRAPHCABRUT": GRAPHCABRUT,
                        "GRAPHCANET": GRAPHCANET,
                    },
                }
            ),
            200,
        )

    except Exception as e:
        return (
            jsonify(
                {
                    "Message": "An error occurred.",
                    "Error": str(e),
                    "Type": str(type(e).__name__),
                }
            ),
            500,
        )

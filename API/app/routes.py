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
        MIXPRODUIT = (VOLNOBLES) / (VOLNOBLES + VOLGRAVES + VOLSTERILE) * 100
        CACAISSE = sum(
            filtered_data[filtered_data["BC"] == "EN ESPECE"]["CA BRUT"].tolist()
        )
        VOYAGESRENDULIV = filtered_data[filtered_data["Chantier"] != "DEPART"].shape[0]
        RECOUVREMENT = sum(filtered_data2["Montant Paye"].tolist())
        return (
            jsonify(
                {
                    "Message": "Balance Sheet",
                    "RECOUVREMENT_Data": filtered_data2.to_dict(orient="records"),
                    "VENTES_Records": len(filtered_data),
                    "RECOUVREMENT_Records": len(filtered_data2),
                    "Metrics": {
                        "CABRUT": CABRUT,
                        "CANET": CANET,
                        "PMVGLOBAL": PMVGLOBAL,
                        "CANOBLES": CANOBLES,
                        "CAGRAVES": CAGRAVES,
                        "VOLNOBLES": VOLNOBLES,
                        "VOLGRAVES": VOLGRAVES,
                        "VOLSTERILE": VOLSTERILE,
                        "PMVHORSSTERILE": PMVHORSSTERILE,
                        "MARGETRANSPORT": MARGETRANSPORT,
                        "QNTENTONNE": QNTENTONNE,
                        "MIXPRODUIT": MIXPRODUIT,
                        "CACAISSE": CACAISSE,
                        "VOYAGESRENDULIV": VOYAGESRENDULIV,
                        "RECOUVREMENTCOMMERCIALE": RECOUVREMENT,
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

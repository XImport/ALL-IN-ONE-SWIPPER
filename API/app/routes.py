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


def List_Division(list1, list2, default_value=0):
    """
    Perform element-wise division between two lists, handling division by zero.

    Args:
        list1 (list): The numerator list.
        list2 (list): The denominator list.
        default_value (float): The value to use when division by zero occurs.

    Returns:
        list: A list containing the results of the division.
    """
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")

    return [
        (num / denom if denom != 0 else default_value)
        for num, denom in zip(list1, list2)
    ]


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
        GRAPHDATEPMV = filtered_data["Date"].unique().tolist()

        daily_sums = (
            filtered_data.groupby(["Date", "Type"])["CA Net"].sum().reset_index()
        )

        # Get a complete list of unique dates
        all_dates = sorted(filtered_data["Date"].unique())

        # Create a DataFrame for all combinations of dates and types
        all_combinations = pd.MultiIndex.from_product(
            [all_dates, ["Nobles", "Graves", "Stérile"]], names=["Date", "Type"]
        )
        complete_data = (
            daily_sums.set_index(["Date", "Type"])
            .reindex(all_combinations, fill_value=0)  # Fill missing values with 0
            .reset_index()
        )

        # Separate the data by type
        GRAPHCANOBLES = complete_data[complete_data["Type"] == "Nobles"][
            "CA Net"
        ].tolist()
        GRAPHCAGRAVES = complete_data[complete_data["Type"] == "Graves"][
            "CA Net"
        ].tolist()
        GRAPHCASTERILE = complete_data[complete_data["Type"] == "Stérile"][
            "CA Net"
        ].tolist()

        daily_volumes = (
            filtered_data.groupby(["Date", "Type"])["Qté en T"].sum().reset_index()
        )

        # Get a complete list of unique dates
        all_dates = sorted(filtered_data["Date"].unique())

        # Create a DataFrame for all combinations of dates and types
        all_combinations = pd.MultiIndex.from_product(
            [all_dates, ["Nobles", "Graves", "Stérile"]], names=["Date", "Type"]
        )
        complete_volumes = (
            daily_volumes.set_index(["Date", "Type"])
            .reindex(all_combinations, fill_value=0)  # Fill missing values with 0
            .reset_index()
        )

        # Separate the data by type
        GRAPHVOLUNOBLES = complete_volumes[complete_volumes["Type"] == "Nobles"][
            "Qté en T"
        ].tolist()
        GRAPHVOLUGRAVES = complete_volumes[complete_volumes["Type"] == "Graves"][
            "Qté en T"
        ].tolist()
        GRAPHVOLUSTERILE = complete_volumes[complete_volumes["Type"] == "Stérile"][
            "Qté en T"
        ].tolist()

        ##################################################################################################################

        CLIENT_TOTAL = filtered_data.groupby("Client")["CA BRUT"].sum().reset_index()

        TOP6_SORTED_CLIENTS = CLIENT_TOTAL.sort_values(
            by="CA BRUT", ascending=False
        ).head(6)

        ##############################################################################################################

        convert_data_json3 = pd.read_excel(files[0], sheet_name="ETAT FINANCIER")

        convert_data_json3["Date"] = pd.to_datetime(
            convert_data_json3["Date"], format="%d/%m/%Y", errors="coerce"
        )

        convert_data_json3["Formatted_Date"] = convert_data_json3["Date"].dt.strftime(
            "%d/%m/%Y"
        )

        search_month = fin_date.month

        filtered_rows = convert_data_json3[
            convert_data_json3["Date"].dt.month == search_month
        ]

        #################################################################################################################
        result = filtered_data.groupby("Produit")["Qté en T"].sum()

        if QNTENTONNE is None or not isinstance(QNTENTONNE, (int, float)):
            raise ValueError("QNTENTONNE must be defined as a valid integer or float")

        # Calculate percentages for QNTBYPRODUIT
        QNTBYPRODUIT = []
        for QNT in result.values.tolist():
            percentage = (int(QNT) / int(QNTENTONNE)) * 100
            QNTBYPRODUIT.append(percentage)

        PRODUITS = result.index.tolist()  # List of "Produit"

        print("Produits:", PRODUITS)
        print("Quantities by Produit (%):", QNTBYPRODUIT)

        ###############################################################################################################

        result2 = filtered_data.groupby("Produit")["CA Net"].sum()
        CANETBYPRODUIT = []
        for CA in result2.values.tolist():
            percentage = (int(CA) / int(CANET)) * 100
            CANETBYPRODUIT.append(percentage)

        ####################################################################################################################

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
                    "PMVGRAPH": {
                        "GRAPHDATEPMV": GRAPHDATEPMV,
                        "PMVNOBLES": List_Division(GRAPHCANOBLES, GRAPHVOLUNOBLES),
                        "PMVGRAVES": List_Division(GRAPHCAGRAVES, GRAPHVOLUGRAVES),
                        "PMVSTERILE": List_Division(GRAPHCASTERILE, GRAPHVOLUSTERILE),
                    },
                    "TOP6CLIENTSGRAPH": {
                        "TOP6CLIENTNAMES": TOP6_SORTED_CLIENTS["Client"].tolist(),
                        "TOP6CLIENTVALUES": TOP6_SORTED_CLIENTS["CA BRUT"].tolist(),
                    },
                    "PERFORMANCECREANCEGRAPH": {
                        "DATES": filtered_rows["Formatted_Date"].to_list(),
                        "RECOUVREMENTCOMMERCIAL": filtered_rows[
                            "Recouvrement Commerciale"
                        ].to_list(),
                        "CREANCECOMMERCIALE": filtered_rows[
                            "Créance Commerciale"
                        ].to_list(),
                        "ENCAISSEMENTFINANCIER": filtered_rows[
                            "Encaissement Financier"
                        ].to_list(),
                    },
                    "QNTBYPRODUITGRAPH": {
                        "PRODUITS": PRODUITS,
                        "QNTBYPRODUIT": QNTBYPRODUIT,
                    },
                    "CANETBYPRODUITGRAPH": {
                        "PRODUITS": PRODUITS,
                        "CANETBYPRODUIT": CANETBYPRODUIT,
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

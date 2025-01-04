import pandas as pd


def prepare_voyages_rendus_data(filtered_data, group_by_month):
    """Prepare voyages rendus chart data."""
    # First filter for non-DEPART Chantier
    rendus_data = filtered_data[filtered_data["Chantier"] != "DEPART"].copy()

    if group_by_month:
        # For monthly aggregation
        rendus_data["Date"] = pd.to_datetime(rendus_data["Date"])
        grouped = (
            rendus_data.groupby(rendus_data["Date"].dt.strftime("%m/%Y"))
            .agg({"Ticket/BL": "count"})  # Count tickets per month
            .reset_index()
        )
    else:
        # For daily aggregation
        grouped = (
            rendus_data.groupby("Date")
            .agg({"Ticket/BL": "count"})  # Count tickets per day
            .reset_index()
        )

    return {
        "GRAPHVOYAGESRENDULIVDATES": grouped["Date"].tolist(),
        "GRAPHVOYAGERENDULIVREE": grouped["Ticket/BL"].tolist(),
        "GRAPHVOYAGERENDUCOMMANDEE": grouped[
            "Ticket/BL"
        ].tolist(),  # Same as livree in this case
    }

from ..Functions.Utils import aggregate_time_series, List_Division


def prepare_pmv_data(filtered_data, group_by_month):
    """Prepare PMV-related chart data."""

    def aggregate_by_type(df, type_name):
        type_data = df[df["Type"] == type_name]
        aggregated = aggregate_time_series(
            type_data, "Date", ["CA Net", "Qté en T"], group_by_month
        )
        return List_Division(
            aggregated["CA Net"].tolist(), aggregated["Qté en T"].tolist()
        )

    dates = aggregate_time_series(filtered_data, "Date", [], group_by_month)[
        "Date"
    ].tolist()

    return {
        "GRAPHDATEPMV": dates,
        "PMVNOBLES": aggregate_by_type(filtered_data, "Nobles"),
        "PMVGRAVES": aggregate_by_type(filtered_data, "Graves"),
        "PMVSTERILE": aggregate_by_type(filtered_data, "Stérile"),
    }

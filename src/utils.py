from datetime import datetime


def filter_by_date(start_date, end_date, lession_list):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return list(
        filter(
            lambda x: start <= datetime.strptime(x["date"], "%Y-%m-%d") <= end,
            lession_list,
        ),
    )

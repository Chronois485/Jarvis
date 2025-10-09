from datetime import datetime


def get_time() -> str:
    return datetime.now().strftime("%H:%M:%S")


def get_date() -> str:
    return datetime.now().strftime("%d/%m/%y")

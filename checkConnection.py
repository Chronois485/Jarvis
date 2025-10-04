import requests


def is_connected_to_internet() -> bool:
    try:
        requests.head("https://google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

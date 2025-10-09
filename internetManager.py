import webbrowser

import requests


class InternetManager:
    def __init__(self) -> None:
        pass

    def is_connected_to_internet(self) -> bool:
        try:
            requests.head("https://google.com", timeout=5)
            return True
        except requests.ConnectionError:
            return False

    def open_link(self, url: str) -> None:
        if url == "" or url == " ":
            return
        webbrowser.open_new_tab(url)

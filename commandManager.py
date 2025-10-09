import json

from internetManager import InternetManager
from clock import get_date, get_time

class CommandManager:
    def __init__(self, commands_table: str) -> None:
        self.internet_manager = InternetManager()
        with open(commands_table, "r") as f:
            self.commands_table: dict = json.load(f)

    def determine_command(self, command: str) -> str:
        user_input: str = ""
        for key, value in self.commands_table.items():
            variants: list = key.split(",")
            for vatiant in variants:
                tmp_key: str = ""
                if ">" in vatiant:
                    key_command = vatiant.split(">")[0]
                    command, user_input = (
                        command[: len(key_command)],
                        command[len(key_command) :],
                    )

                    if tmp_key in command:
                        return value.replace(">", user_input)
                else:
                    tmp_key = vatiant
                    if tmp_key == command:
                        return value
        return ""

    def run_command(self, command: str) -> str | None:
        command_with_input: list[str] = []
        if ":" in command:
            command_with_input = command.split(":")
        if command_with_input:
            if command_with_input[0] == "FIND_IN_INTERNET":
                self.internet_manager.open_link(
                    f"https://www.google.com/search?q={command_with_input[1].replace(" ", "+")}"
                )
                return
        else:
            if command == "WHAT_DATE":
                return f"Сьогодні {get_date()}"
            elif command == "WHAT_TIME":
                return f"Зараз {get_time()}"


if __name__ == "__main__":
    manager = CommandManager("./commands.json")

    print(manager.determine_command("яке число"))
    print(manager.determine_command("дата"))
    print(manager.determine_command("котра година"))
    print(manager.determine_command("година"))
    print(manager.determine_command("час"))
    find_test = manager.determine_command("знайди парабола")
    print(manager.determine_command("пошукай парабола"))
    print(find_test)
    manager.run_command(find_test)
    print(manager.run_command("WHAT_TIME"))
    print(manager.run_command("WHAT_DATE"))

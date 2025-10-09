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
                key_command: str = ""
                if ">" in vatiant:
                    key_command = vatiant.split(">")[0]
                    command, user_input = (
                        command[: len(key_command)],
                        command[len(key_command) :],
                    )

                    if key_command in command:
                        return value.replace(">", user_input)
                else:
                    key_command = vatiant
                    if key_command == command:
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
                return "Відкриваю"
        else:
            if command == "WHAT_DATE":
                return f"Сьогодні {get_date()}"
            elif command == "WHAT_TIME":
                return f"Зараз {get_time()}"
            elif command == "EXIT":
                return f"До побачення"

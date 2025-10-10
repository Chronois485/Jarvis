import json

import constants as const
from internetManager import InternetManager
from clock import get_date, get_time


class CommandManager:
    def __init__(self, commands_table: str) -> None:
        self.internet_manager = InternetManager()
        with open(commands_table, "r") as f:
            self.commands_table: dict = json.load(f)

    def determine_command(self, command: str) -> str:
        for key, value in self.commands_table.items():
            variants: list = key.split(",")
            for variant in variants:
                if ">" in variant:
                    key_command: str = variant.split(">")[0]
                    command, user_input = (
                        command[: len(key_command)],
                        command[len(key_command):],
                    )

                    if key_command in command:
                        return value.replace(">", user_input)
                else:
                    key_command: str = variant
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
                    const.GOOGLE_FIND.format(promt=command_with_input[1].replace(" ", "+"))
                )
                return const.ANSWER_OPEN.format(name=const.SETTINGS_MANAGER.get_settings("name"))
            return None
        else:
            if command == "WHAT_DATE":
                return const.ANSWER_WHAT_DATE.format(name=const.SETTINGS_MANAGER.get_settings("name"), date=get_date())
            elif command == "WHAT_TIME":
                return const.ANSWER_WHAT_TIME.format(name=const.SETTINGS_MANAGER.get_settings("name"), date=get_time())
            elif command == "EXIT":
                return const.ANSWER_EXIT.format(name=const.SETTINGS_MANAGER.get_settings("name"))
            return None

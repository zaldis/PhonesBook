import argparse
import pathlib
from typing import Dict

import handlers
import managers
from utils.log import logging


help_message = (
"""
The phone program to save phone numbers of your friends

Allowed commands:
  > get - allows filter and get your contacts:
        Arguments:
            * filter_key: phone_number | full_name
            * filter_value: substring of necessary data

  > set - allows adding new contacts:
        Arguments:
            * phone_number
            * full_name
            * address

  > exit - stop the program
"""
)

class CommandError(ValueError):
    pass


class PhonesBookRunner:
    EXIT_COMMAND = 'exit'
    GET_COMMAND = 'get'
    SET_COMMAND = 'set'

    command_map: Dict[str, handlers.BaseCommandHandler] = {
        EXIT_COMMAND: handlers.ExitCommandHandler(),
        GET_COMMAND: handlers.GetCommandHandler(),
        SET_COMMAND: handlers.SetCommandHandler(),
    }

    def __init__(self) -> None:
        self._init_managers()
        self._command = ''

    def _init_managers(self):
        parser = argparse.ArgumentParser(description='PhonesBook system to save your contacts')
        parser.add_argument('-s', '--storage', type=str, help='File name to load/store your contacts')
        arguments = parser.parse_args()

        STORAGE_FILE_NAME = arguments.storage or 'phones'
        PROJECT_ROOT_FOLDER = pathlib.Path(__file__).parent.resolve()
        STORAGE_FILE_PATH = f'{PROJECT_ROOT_FOLDER}/{STORAGE_FILE_NAME}.json'
        LOG_FILE_PATH = f'{PROJECT_ROOT_FOLDER}/{STORAGE_FILE_NAME}.log'

        managers.Printer.init_printer(
            log_path=LOG_FILE_PATH,
            storage_path=STORAGE_FILE_PATH,
        )
        managers.Reader.init_reader(
            storage_path=STORAGE_FILE_PATH
        )

    @property
    def command(self) -> str:
        return self._command

    @command.setter
    def command(self, new_command: str) -> None:
        allowed_commands = (
            self.GET_COMMAND,
            self.SET_COMMAND,
            self.EXIT_COMMAND,
        )
        if new_command not in allowed_commands:
            raise CommandError(f'The "{new_command}" command is not allowed')
        self._command = new_command

    @logging('Runner')
    def run(self):
        managers.ContactManager.load_contacts()
        while True:
            self._ask_new_command()
            if not self.command:
                continue
 
            self.command_map[self.command].handle()
 
            if self.command == self.EXIT_COMMAND:
                break

    def _ask_new_command(self):
        try:
            self.command = managers.Reader.read_from_user('Enter the command: ')
        except CommandError as err:
            managers.Printer.print_info(f'warning> {err}')
            managers.Printer.print_info(help_message)


if __name__ == '__main__':
    runner = PhonesBookRunner()
    runner.run()


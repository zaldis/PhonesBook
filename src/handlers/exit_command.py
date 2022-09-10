import json
from dataclasses import asdict

from .base import BaseCommandHandler
from managers import ContactManager, Printer
from utils.log import logging


class ExitCommandHandler(BaseCommandHandler):
    @logging('Exit command')
    def handle(self) -> None:
        Printer.print_info(f'Saving the data into {Printer._storage_path} file ...')
        contacts = ContactManager.get_contacts()
        raw_contacts = [asdict(contact) for contact in contacts]
        save_text = json.dumps(raw_contacts, indent=2)
        Printer.print_storage(save_text)
        Printer.print_info(f'The data was saved into {Printer._storage_path} file')
        Printer.print_info('Bye Bye sweet user')


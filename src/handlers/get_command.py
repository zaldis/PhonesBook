from prettytable import PrettyTable

from .base import BaseCommandHandler
from managers import ContactManager, Printer, Reader
from utils.log import logging


class GetCommandHandler(BaseCommandHandler):
    @logging('Get command')
    def handle(self) -> None:
        filter_key = Reader.read_from_user('get> Enter your filter key: ')
        filter_value = Reader.read_from_user('get> Enter your filter value: ')
        filtered_contacts = ContactManager.get_contacts(filter_key, filter_value)

        Printer.print_info(f'\n>>> Found contacts:')
        contacts_table = PrettyTable()
        contacts_table.field_names = ['#', 'full_name', 'number', 'address']
        for pos, contact in enumerate(filtered_contacts, start=1):
            contacts_table.add_row([
                pos,
                contact.full_name,
                contact.phone_number,
                contact.address
            ])
        Printer.print_info(str(contacts_table))
        Printer.print_info(f'<<< Found contacts\n')


from prettytable import PrettyTable

from utils import contact as contact_utils
from utils.log import logging


@logging
def handle_get_command() -> None:
    filter_key = input('get> Enter your filter key: ')
    filter_value = input('get> Enter your filter value: ')
    filtered_contacts = contact_utils.get_contacts(filter_key, filter_value)

    print(f'\n>>> Found contacts:')
    contacts_table = PrettyTable()
    contacts_table.field_names = ['#', 'full_name', 'number', 'address']
    for pos, contact in enumerate(filtered_contacts, start=1):
        contacts_table.add_row([
            pos,
            contact['full_name'],
            contact['phone_number'],
            contact['address']
        ])
    print(contacts_table)
    print(f'<<< Found contacts\n')


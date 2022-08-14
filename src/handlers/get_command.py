from utils import contact as contact_utils
from utils.log import logging


@logging
def handle_get_command() -> None:
    filter_key = input('get> Enter your filter key: ')
    filter_value = input('get> Enter your filter value: ')
    filtered_contacts = contact_utils.get_contacts(filter_key, filter_value)

    print(f'\n>>> Found contacts:')
    for pos, contact in enumerate(filtered_contacts, start=1):
        print(f'#{pos}')
        print(contact['full_name'])
        print(f'\tPhone number:\t{contact["phone_number"]}')
        print(f'\tAddress:\t{contact["address"]}')
        print()
    print(f'<<< Found contacts\n')


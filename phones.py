import json
import pathlib
from typing import Iterable, Dict
from pprint import pprint


contacts = []

CURRENT_FOLDER = pathlib.Path(__file__).parent.resolve()
STORAGE_FILE_NAME = 'phones.json'
STORAGE_FILE_PATH = f'{CURRENT_FOLDER}/{STORAGE_FILE_NAME}'


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


def filter_contacts_by_field(field: str, value: str) -> Iterable[Dict[str, str]]:
    founded_contacts = []
    for contact in contacts:
        if value.lower() in contact[field].lower():
            founded_contacts.append(contact)
    return founded_contacts


def get_contacts(filter_key: str, filter_value: str) -> Iterable[Dict[str, str]]:
    if filter_key not in ['full_name', 'phone_number']:
        found_contacts = contacts
    else:
        found_contacts = filter_contacts_by_field(filter_key, filter_value)
    return sorted(
        found_contacts,
        key=lambda contact: contact['full_name'].lower()
    )


def set_contact(phone_number: str, full_name: str, address: str) -> None:
    global contacts

    contacts.append({
        'phone_number': phone_number,
        'full_name': full_name,
        'address': address,
    })


def get_command(message: str = 'Enter the command: ') -> str:
    command = input('Enter your command: ')
    
    allowed_commands = ('get', 'set', 'exit', )
    if command not in allowed_commands:
        raise CommandError(f'The "{command}" command is not allowed')
    return command


def handle_new_command() -> str:
    command = ''
    try:
        command = get_command()
    except CommandError as err:
        print(f'warning> {err}')
        print(help_message)
    return command 


def handle_exit_command() -> None:
    print(f'Saving the data into {STORAGE_FILE_PATH} file ...')
    file = open(STORAGE_FILE_PATH, 'w')
    save_text = json.dumps(contacts, indent=2)
    file.write(save_text)
    file.close()
    print(f'The data was saved into {STORAGE_FILE_PATH} file')
    print('Bye Bye sweet user')


def handle_get_command() -> None:
    filter_key = input('get> Enter your filter key: ')
    filter_value = input('get> Enter your filter value: ')
    filtered_contacts = get_contacts(filter_key, filter_value)

    print(f'\n>>> Found contacts:')
    for pos, contact in enumerate(filtered_contacts, start=1):
        print(f'#{pos}')
        print(contact['full_name'])
        print(f'\tPhone number:\t{contact["phone_number"]}')
        print(f'\tAddress:\t{contact["address"]}')
        print()
    print(f'<<< Found contacts\n')


def handle_set_command() -> None:
    phone_number = input('set> Enter phone number: ')
    full_name = input('set> Enter full name: ')
    address = input('set> Enter address: ')
    set_contact(phone_number, full_name, address)
    print('New contact was successfuly added')


def handle_init_contacts():
    global contacts
    print(f'Loading contacts from: {STORAGE_FILE_PATH}...')
    file = open(STORAGE_FILE_PATH, 'r')
    stringified_contacts = file.read()
    contacts = json.loads(stringified_contacts)
    print(f'Contacs was loaded')


command_map = {
    'exit': handle_exit_command,
    'get': handle_get_command,
    'set': handle_set_command,
}


def run():
    handle_init_contacts()

    while True:
        command = handle_new_command()
        if not command:
            continue
        
        command_map[command]()
        
        if command == 'exit':
            break


if __name__ == '__main__':
    run()

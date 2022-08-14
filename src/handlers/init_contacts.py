import json

import settings


def handle_init_contacts():
    print(f'Loading contacts from: {settings.STORAGE_FILE_PATH}...')
    try:
        file = open(settings.STORAGE_FILE_PATH, 'r')
    except FileNotFoundError:
        print('File does not exist')
    else:
        stringified_contacts = file.read()
        settings.contacts = json.loads(stringified_contacts)
        print(f'Contacs was loaded')


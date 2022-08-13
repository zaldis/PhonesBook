import json

import settings


def handle_init_contacts():
    print(f'Loading contacts from: {settings.STORAGE_FILE_PATH}...')
    file = open(settings.STORAGE_FILE_PATH, 'r')
    stringified_contacts = file.read()
    settings.contacts = json.loads(stringified_contacts)
    print(f'Contacs was loaded')


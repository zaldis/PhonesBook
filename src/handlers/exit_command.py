import json

import settings
from utils.log import logging


@logging
def handle_exit_command() -> None:
    print(f'Saving the data into {settings.STORAGE_FILE_PATH} file ...')
    file = open(settings.STORAGE_FILE_PATH, 'w')
    save_text = json.dumps(settings.contacts, indent=2)
    file.write(save_text)
    file.close()
    print(f'The data was saved into {settings.STORAGE_FILE_PATH} file')
    print('Bye Bye sweet user')


import json

import settings
from utils.log import logging


@logging
def handle_exit_command() -> None:
    print(f'Saving the data into {settings.STORAGE_FILE_PATH} file ...')
    with open(settings.STORAGE_FILE_PATH, 'w') as file_obj:
        save_text = json.dumps(settings.contacts, indent=2)
        file_obj.write(save_text)
    print(f'The data was saved into {settings.STORAGE_FILE_PATH} file')
    print('Bye Bye sweet user')


import pathlib


contacts = []


PROJECT_ROOT_FOLDER = pathlib.Path(__file__).parent.parent.resolve()
STORAGE_FILE_NAME = 'phones.json'
STORAGE_FILE_PATH = f'{PROJECT_ROOT_FOLDER}/{STORAGE_FILE_NAME}'


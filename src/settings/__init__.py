import pathlib
import sys


contacts = []


PROJECT_ROOT_FOLDER = pathlib.Path(__file__).parent.parent.resolve()
STORAGE_FILE_NAME = 'phones'


def init_settings():
    global STORAGE_FILE_NAME
    global STORAGE_FILE_PATH
    global LOG_FILE_PATH

    if len(sys.argv) > 1:
        STORAGE_FILE_NAME = sys.argv[1]

    STORAGE_FILE_PATH = f'{PROJECT_ROOT_FOLDER}/{STORAGE_FILE_NAME}.json'
    LOG_FILE_PATH = f'{PROJECT_ROOT_FOLDER}/{STORAGE_FILE_NAME}.log'


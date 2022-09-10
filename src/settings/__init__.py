import argparse
import pathlib


contacts = []


PROJECT_ROOT_FOLDER = pathlib.Path(__file__).parent.parent.resolve()
STORAGE_FILE_NAME = 'phones'


def init_settings():
    global STORAGE_FILE_NAME
    global STORAGE_FILE_PATH
    global LOG_FILE_PATH

    parser = argparse.ArgumentParser(description='PhonesBook system to save your contacts')
    parser.add_argument('-s', '--storage', type=str, help='File name to load/store your contacts')
    argumets = parser.parse_args()

    if argumets.storage:
        STORAGE_FILE_NAME = argumets.storage

    STORAGE_FILE_PATH = f'{PROJECT_ROOT_FOLDER}/{STORAGE_FILE_NAME}.json'
    LOG_FILE_PATH = f'{PROJECT_ROOT_FOLDER}/{STORAGE_FILE_NAME}.log'


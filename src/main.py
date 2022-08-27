import handlers
import settings
from utils.log import logging


@logging
def run():
    command_map = {
        'exit': handlers.handle_exit_command,
        'get': handlers.handle_get_command,
        'set': handlers.handle_set_command,
    }
    handlers.handle_init_contacts()

    while True:
        command = handlers.handle_new_command()
        if not command:
            continue
        
        command_map[command]()
        
        if command == 'exit':
            break


if __name__ == '__main__':
    settings.init_settings()
    run()


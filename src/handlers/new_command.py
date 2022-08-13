def get_command(ask_command_message: str = 'Enter the command: ') -> str:
    command = input(ask_command_message)
    
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


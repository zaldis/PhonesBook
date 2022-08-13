from .exit_command import handle_exit_command
from .get_command import handle_get_command
from .init_contacts import handle_init_contacts
from .new_command import handle_new_command
from .set_command import handle_set_command


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



__all__ = [
    'handle_new_command',
    'handle_exit_command',
    'handle_get_command',
    'handle_set_command',
    'handle_init_contacts',
]


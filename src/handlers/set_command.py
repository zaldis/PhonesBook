from utils import contact as contact_utils


def handle_set_command() -> None:
    phone_number = input('set> Enter phone number: ')
    full_name = input('set> Enter full name: ')
    address = input('set> Enter address: ')
    contact_utils.set_contact(phone_number, full_name, address)
    print('New contact was successfuly added')


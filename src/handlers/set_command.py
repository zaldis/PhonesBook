from handlers.base import BaseCommandHandler
from managers import Contact, ContactManager, Printer, Reader


class SetCommandHandler(BaseCommandHandler):
    def handle(self) -> None:
        phone_number = Reader.read_from_user('set> Enter phone number: ')
        full_name = Reader.read_from_user('set> Enter full name: ')
        address = Reader.read_from_user('set> Enter address: ')
        contact = Contact(
            phone_number=phone_number,
            full_name=full_name,
            address=address
        )
        ContactManager.add_contact(contact)
        Printer.print_info('New contact was successfuly added')


import json
from dataclasses import dataclass
from typing import Sequence


@dataclass
class Contact:
    full_name: str
    phone_number: str
    address: str


class ContactManager:
    _contacts = []

    @classmethod
    def load_contacts(cls) -> None:
        from managers import Reader, Printer
        Printer.print_info(f'Loading contacts from: {Reader._storage_path}...')
        stringified_contacts = Reader.read_contacts()
        raw_contacts = json.loads(stringified_contacts)
        for raw_contact in raw_contacts:
            contact = Contact(
                full_name=raw_contact['full_name'],
                phone_number=raw_contact['phone_number'],
                address=raw_contact['address'],
            )
            ContactManager.add_contact(contact)
        Printer.print_info(f'Contacs was loaded')

    @classmethod
    def add_contact(cls, new_contact: Contact) -> None:
        cls._contacts.append(new_contact)

    @classmethod
    def get_contacts(cls, filter_key: str = '', filter_value: str = '') -> Sequence[Contact]:
        if filter_key not in ['full_name', 'phone_number']:
            return cls._contacts

        found_contacts = cls._filter_contacts_by_field(filter_key, filter_value)
        return sorted(
            found_contacts,
            key=lambda contact: contact.full_name.lower()
        )

    @classmethod
    def _filter_contacts_by_field(cls, field: str, value: str) -> Sequence[Contact]:
        founded_contacts = []
        for contact in cls._contacts:
            contact_value = getattr(contact, field, '')
            if value.lower() in contact_value:
                founded_contacts.append(contact)
        return founded_contacts


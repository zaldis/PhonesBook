from typing import Iterable, Dict

import settings


def get_contacts(filter_key: str, filter_value: str) -> Iterable[Dict[str, str]]:
    if filter_key not in ['full_name', 'phone_number']:
        found_contacts = settings.contacts
    else:
        found_contacts = _filter_contacts_by_field(filter_key, filter_value)
    return sorted(
        found_contacts,
        key=lambda contact: contact['full_name'].lower()
    )


def _filter_contacts_by_field(field: str, value: str) -> Iterable[Dict[str, str]]:
    founded_contacts = []
    for contact in settings.contacts:
        if value.lower() in contact[field].lower():
            founded_contacts.append(contact)
    return founded_contacts


def set_contact(phone_number: str, full_name: str, address: str) -> None:
    settings.contacts.append({
        'phone_number': phone_number,
        'full_name': full_name,
        'address': address,
    })


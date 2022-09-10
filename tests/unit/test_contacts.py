import unittest

from managers import ContactManager, Contact


class TestContactsFiltration(unittest.TestCase):

    def setUp(self) -> None:
        ContactManager._contacts = [
            Contact(
                full_name="Anton Bera",
                phone_number="28474927293",
                address="anton street"
            ),
            Contact(
                full_name="Ivan Bobrov",
                phone_number="87493012702",
                address="ivan bobrov",
            ),
            Contact(
                full_name="Bill Smith",
                phone_number="739327104729",
                address="bill smith"
            ),
            Contact(
                full_name="Anton Junior",
                phone_number="74937297392743",
                address="anton junior",
            )
        ]
        return super().setUp()

    def test_no_contacts(self):
        ContactManager._contacts = []

        found_contacts = ContactManager.get_contacts("full_name", "Anton")
 
        self.assertEqual(
            len(list(found_contacts)), 0,
            'If no contacts are loaded, then no contact can be found'
        )

    def test_incorrect_filtration_key(self):
        invalid_filtration_key = "fulll_name"
        contacts_count = len(ContactManager._contacts)

        found_contacts = ContactManager.get_contacts(invalid_filtration_key, "Anton")

        self.assertEqual(
            len(list(found_contacts)), contacts_count,
            'If filtration key is invalid, all contacts should be found'
        )

    def test_single_name(self):
        filtration_key = 'full_name'
        filtration_value = 'iVaN'
    
        found_contacts = ContactManager.get_contacts(filtration_key, filtration_value)

        self.assertEqual(
            len(list(found_contacts)), 1,
            'There is only one Ivan contanct in the contacts'
        )

    def test_few_names(self):
        filtration_key = 'full_name'
        filtration_value = 'anTON'

        found_contacts = ContactManager.get_contacts(filtration_key, filtration_value)

        self.assertEqual(
            len(list(found_contacts)), 2,
            'There are only two Anton contacts in the contacts'
        )

    def test_no_name(self):
        pass

    def test_single_phone_number(self):
        pass

    def test_few_phone_numbers(self):
        pass
    
    def test_no_phone_number(self):
        pass

    def test_few_names_few_phone_numbers(self):
        pass


class TestAddingNewContacts(unittest.TestCase):

    def setUp(self) -> None:
        ContactManager._contacts = [
            Contact(
                full_name="Anton Bera",
                phone_number="28474927293",
                address="anton street"
            )
        ]
        return super().setUp()

    def test_adding_1_contact(self):
        start_contacts_count = len(ContactManager._contacts)

        new_contact = Contact(
            phone_number="333222888",
            full_name="Ivan Bobrov",
            address="ivan bobrov"
        )
        ContactManager.add_contact(new_contact)

        end_contacts_count = len(ContactManager._contacts)
        self.assertEqual(
            start_contacts_count + 1, end_contacts_count,
            'After adding new contact the contacts count should be increased by 1'
        )

    def test_adding_2_contacts(self):
        pass

    def test_adding_4_contacts(self):
        pass


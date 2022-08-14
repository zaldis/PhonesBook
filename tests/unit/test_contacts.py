import unittest
import settings
from src.utils.contact import filter_contacts_by_field


class TestContactsFiltration(unittest.TestCase):

    def setUp(self) -> None:
        settings.contacts = [
            {
                "full_name": 'Anton Bera',
                "phone_number": "28474927293",
                "address": "anton street"
            }
        ]
        return super().setUp()

    def test_empty_list(self):
        settings.contacts = []

        found_contacts = filter_contacts_by_field("full_name", "Anton")
 
        self.assertIs(
            len(found_contacts), 0,
            'If no contacts are loaded, then no contacts can be found'
        )


import unittest
# from unittest.mock import patch
# from src.utils.contact import filter_contacts_by_field


class TestContactsFiltration(unittest.TestCase):
    
    def test_somethings(self):
        self.assertTrue(5 != 6, '5 != 6')

    def test_somethings2(self):
        self.assertFalse(5 == 6, '5 == 6')

    def test_lists(self):
        self.assertListEqual([1, 2, 3], [1, 2, 30], 'Lists are not equal')


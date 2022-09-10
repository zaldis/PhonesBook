import unittest
from pathlib import Path

from managers import Printer
from utils.log import logging


LOG_MESSAGE = 'my message'
counter = 0
@logging(LOG_MESSAGE)
def target_function():
    global counter
    counter += 1


class TestActionsLogging(unittest.TestCase):

    def setUp(self) -> None:
        Printer._log_path = 'tests/testing-log-file.log'

    def tearDown(self) -> None:
        testing_log_file = Path(Printer._log_path)
        testing_log_file.unlink()

    def test_logging_calls_origin_function(self):
        inititial_counter = counter

        target_function()
        target_function()

        self.assertEqual(inititial_counter + 2, counter)


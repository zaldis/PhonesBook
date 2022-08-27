import unittest
from pathlib import Path

import settings
from utils.log import logging


counter = 0
@logging
def target_function():
    global counter
    counter += 1


class TestActionsLogging(unittest.TestCase):

    def setUp(self) -> None:
        settings.LOG_FILE_PATH = 'tests/testing-log-file.log'

    def tearDown(self) -> None:
        testing_log_file = Path(settings.LOG_FILE_PATH)
        testing_log_file.unlink()

    def test_logging_calls_origin_function(self):
        inititial_counter = counter

        target_function()
        target_function()

        self.assertEqual(inititial_counter + 2, counter)


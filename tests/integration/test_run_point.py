import unittest
from pathlib import Path
from unittest.mock import patch

from main import run
import settings


class TestRunPoint(unittest.TestCase):

    def setUp(self) -> None:
        settings.LOG_FILE_PATH = 'tests/test-logs.log' 

    def tearDown(self) -> None:
        logs_file = Path(settings.LOG_FILE_PATH)
        logs_file.unlink()

    @patch('handlers.handle_new_command')
    @patch('handlers.handle_init_contacts')
    @patch('handlers.handle_exit_command')
    def test_simple_exit(
        self,
        mocked_exit_command_handler,
        mocked_init_contacts_handler,
        mocked_new_command_handler
    ):
        mocked_new_command_handler.return_value = 'exit'

        run()

        logs_file = Path(settings.LOG_FILE_PATH)
        self.assertTrue(logs_file.is_file())
        self.assertTrue(mocked_exit_command_handler.called)


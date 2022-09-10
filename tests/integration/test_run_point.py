import unittest
from pathlib import Path
from unittest.mock import patch

from managers import Printer
from main import PhonesBookRunner


class TestRunPoint(unittest.TestCase):

    def tearDown(self) -> None:
        if Printer._log_path:
            logs_file = Path(Printer._log_path)
            logs_file.unlink()

    @patch('managers.ContactManager.load_contacts')
    @patch('managers.Reader.read_from_user')
    @patch('handlers.ExitCommandHandler.handle')
    @patch('argparse.ArgumentParser')
    def test_simple_exit(
        self,
        mocked_argument_parser,
        mocked_load_contacts,
        mocked_read_from_user,
        mocked_exit_handler
    ):
        self.runner = PhonesBookRunner()
        Printer.init_printer(
            storage_path='tests/storage_path.json',
            log_path='tests/log_path.log'
        )
        mocked_read_from_user.return_value = 'exit'

        self.runner.run()

        self.assertIsNotNone(Printer._log_path)
        logs_file = Path(Printer._log_path)
        self.assertTrue(logs_file.is_file())
        self.assertTrue(mocked_exit_handler.called)
        self.assertTrue(mocked_load_contacts.called)


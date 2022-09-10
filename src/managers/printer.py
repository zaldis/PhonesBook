class Printer:
    _storage_path = None
    _log_path = None

    @classmethod
    def init_printer(cls, storage_path: str, log_path: str) -> None:
        cls._storage_path = storage_path
        cls._log_path = log_path

    @classmethod
    def print_info(cls, text: str) -> None:
        print(text)

    @classmethod
    def print_log(cls, text: str) -> None:
        if not cls._log_path:
            raise Exception('Can not be used before initialization')

        with open(cls._log_path, 'a') as file_obj:
            file_obj.write(text)

    @classmethod
    def print_storage(cls, text: str) -> None:
        if not cls._storage_path:
            raise Exception('Can not be used before initialization')

        with open(cls._storage_path, 'w') as file_obj:
            file_obj.write(text)


class Reader:

    _storage_path = None

    @classmethod
    def init_reader(cls, storage_path: str) -> None:
        cls._storage_path = storage_path

    @classmethod
    def read_contacts(cls) -> str:
        if not cls._storage_path:
            raise Exception('Can not read from storage before initialization')
        with open(cls._storage_path, 'r') as file_obj:
            raw_contacts = file_obj.read()
        return raw_contacts
    
    @classmethod
    def read_from_user(cls, message: str) -> str:
        return input(message)


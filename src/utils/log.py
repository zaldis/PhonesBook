import datetime as dt
from functools import wraps
from typing import Callable

from managers import Printer


class logging:
    def __init__(self, message: str) -> None:
        self._message = message

    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            stringified_now = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            Printer.print_log(
                f'[{stringified_now}] <{self._message}> is started\n'
            )

            result = func(*args, **kwargs)

            stringified_now = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            Printer.print_log(
                f'[{stringified_now}] <{self._message}> is ended\n'
            )
            return result
        return wrapper


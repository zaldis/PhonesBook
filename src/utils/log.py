import datetime as dt
from functools import wraps


import settings


def logging(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        stringified_now = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(settings.LOG_FILE_PATH, 'a') as log_file:
            log_file.write(f'[{stringified_now}] Function <{func.__name__}> is started\n')

        result = func(*args, **kwargs)

        stringified_now = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # log_file = open(settings.LOG_FILE_PATH, 'a')
        # log_file.write(f'[{stringified_now}] Function <{func.__name__}> is ended\n')
        # log_file.close()
        with open(settings.LOG_FILE_PATH, 'a') as log_file:
            log_file.write(f'[{stringified_now}] Function <{func.__name__}> is ended\n')
        return result

    return wrapper

import datetime
import logging
import random
import string
from time import sleep


# RANDOM
def random_num():
    """Generate random number"""
    return str(random.randint(1111111, 9999999))


def random_str(length=5):
    """Generate random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


# WAIT
def wait_until_ok(timeout=5, period=0.5):
    """Reties until OK"""

    log = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        log.error(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator


# USERS
class User:

    def __init__(self, login="", phone="", password=""):
        self.login = login
        self.phone = phone
        self.password = password

    def random_user_data(self, login="", phone="", password=""):
        """Fill user with sample data and values if provided"""
        user = random_str()
        self.login = f"{user}" if not login else login
        self.phone = f"97{random_num()}" if not phone else phone
        self.password = f"{random_str(4)}{random_num()}" if not password else password

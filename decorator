from functools import wraps
from random import randint


def log(message_sample: str):
    """
    возвращает функцию декоратор
    """
    def decorator(func):
        """
        декоратор
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            p = randint(10, 30)
            print(f' {message_sample} {p}с ')
        return wrapper

    return decorator

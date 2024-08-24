from datetime import time
from functools import wraps


def log(filename=None):
    """Декороратор логирует начало и конец работы функции"""
    def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                start_time = time()
                result = func(*args, **kwargs)
                stop_time = time()
                log_message = (
                    f"Function '{func.__name__}' started at {start_time}\n"
                    f"Function '{func.__name__}' finished at {stop_time}\n"
                    f"Result: {result}\n"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message + "\n")
            except Exception as e:
                error_message = (
                    f"Function '{func.__name__}' raised an error: {type(e).__name__} - {e}\n"
                    f"Inputs: args={args}, kwargs={kwargs}\n"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_message + "\n")
                else:
                    print(error_message + "\n")
                raise
            return result

        return wrapper

    return timer

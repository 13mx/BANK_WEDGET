import functools
import datetime


def log(filename=None):
    def decorator_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            error = None
            try:
                result = func(*args, **kwargs)
                status = 'ok'
            except Exception as e:
                error = str(e)
                status = 'error'

            log_message = f"{func.__name__} {status}"
            if error:
                log_message += f": {error}. Inputs: {args}, {kwargs}"

            if filename:
                with open(filename, 'a') as f:
                    f.write(f"{datetime.datetime.now()}: {log_message}\n")
            else:
                print(f"{datetime.datetime.now()}: {log_message}")

            return result

        return wrapper

    return decorator_log


# Пример использования
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

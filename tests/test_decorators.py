import os
from decorators.function_logs import my_function


def test_my_function():
    # Test the function result
    assert my_function(2, 3) == 5, "Should be 5"


def test_my_function_error():
    # Test the function with inputs that cause an error to check the logging
    try:
        my_function('a', 3)
    except TypeError:
        pass
    # Check if the error log exists
    assert os.path.isfile('mylog.txt'), "Log file should exist"


def test_my_function_log_content():
    # Run the function
    my_function(4, 5)
    # Check if the correct log is written
    with open('mylog.txt', 'r') as f:
        logs = f.readlines()
    assert "my_function ok" in logs[-1], "Log should contain function status 'ok'"


def test_my_function_log_error_content():
    # Cause an error
    try:
        my_function('a', 3)
    except TypeError:
        pass
    # Check the log content for the error
    with open('mylog.txt', 'r') as f:
        logs = f.readlines()
    assert "my_function error" in logs[-1], "Log should contain function status 'error'"

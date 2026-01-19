import pytest
from lib.password_checker import *

"""
Password is equal or longer than 8 char
"""
def test_password_checker_8_char_long():
    password_checker = PasswordChecker()
    assert password_checker.check("12345678") == True

"""
Password is not 8 char
"""
def test_password_checker_less_than_8_char():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("1234567")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
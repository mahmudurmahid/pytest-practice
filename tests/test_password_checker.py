from lib.password_checker import *

"""
Password is equal or longer than 8 char
"""
def test_password_checker_8_char_long():
    password_checker = PasswordChecker()
    assert password_checker.check("12345678") == True

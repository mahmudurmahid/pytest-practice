from lib.check_codeword import *

def test_check_codeword_return_correct_come_in_for_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_return_close_but_nope_for_haste():
    result = check_codeword("haste")
    assert result == "Close, but nope."

def test_check_codeword_return_wrong_for_donkey():
    result = check_codeword("monkey")
    assert result == "WRONG!"

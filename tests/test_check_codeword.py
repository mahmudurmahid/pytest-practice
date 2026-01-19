from lib.check_codeword import *

"""
If codeword is correct,
returns 'Corect! Come in.'
"""
def test_check_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

"""
If codeword is close,
returns 'Close, but nope.'
"""
def test_check_close_codeword():
    result = check_codeword("haste")
    assert result == "Close, but nope."

"""
If codeword is wrong,
returns 'WRONG!'
"""
def test_check_codeword_wrong_codeword():
    result = check_codeword("monkey")
    assert result == "WRONG!"

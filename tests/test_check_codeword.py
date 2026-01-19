from lib.check_codeword import *

def test_check_codeword_return_correct_come_in_for_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

from lib.report_length import *

"""
If report length is correct,
returns correct character length
"""
def test_report_length_correct():
    result = report_length("hello, world")
    assert result == "This string was 12 characters long."
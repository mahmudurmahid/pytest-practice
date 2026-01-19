import pytest
from lib.present import *

"""
Wrap and unwrap a present
"""
def test_present_wrap_and_unwrap():
    present = Present()
    present.wrap("football")
    assert present.unwrap() == "football"

"""
Wrapping a present twice should raise an exception
"""
def test_present_wrap_for_already_wrapped_present():
    present = Present()
    present.wrap("football")
    with pytest.raises(Exception) as e:
        present.wrap("football")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

"""
Unwrapping a present before anything is wrapped should raise an exception
"""
def test_present_unwrap_for_no_existing_present():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."
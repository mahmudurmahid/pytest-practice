from lib.gratitudes import *

"""
Initially, an empty list appears with opener
"""
def test_gratitude_for_empty_string():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

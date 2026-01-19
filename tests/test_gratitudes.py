from lib.gratitudes import *

"""
Initially, an empty list appears with opener
"""
def test_gratitude_for_empty_string():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

"""
Adding one string to return one gratitude
"""
def test_gratitute_adding_one_string():
    gratitudes = Gratitudes()
    gratitudes.add("your health")
    assert gratitudes.format() == "Be grateful for: your health"
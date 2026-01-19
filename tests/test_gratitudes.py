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

"""
Adding multiple strings to return multiple gratitudes in a list
"""
def test_gratitudes_adding_multiple_strings():
    gratitudes = Gratitudes()
    gratitudes.add("your family")
    gratitudes.add("your health")
    assert gratitudes.format() == "Be grateful for: your family, your health"
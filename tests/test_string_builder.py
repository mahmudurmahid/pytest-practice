from lib.string_builder import *

"""
Initially output is an empty string
"""
def test_string_builder_for_initial_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

"""
When a string is added, output is the same string
"""
def test_string_builder_to_return_same_string():
    string_builder = StringBuilder()
    string_builder.add("hello, world!")

    assert string_builder.output() == "hello, world!"

"""
When a string is added, size of the string is returned
"""
def test_string_builder_to_return_size():
    string_builder = StringBuilder()
    string_builder.add("hello, world!")

    assert string_builder.size() == 13
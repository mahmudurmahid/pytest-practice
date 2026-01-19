from lib.greet import *

def test_greet_returns_hello_mark_for_mark():
    result = greet("mark")
    assert result == "Hello, mark!"
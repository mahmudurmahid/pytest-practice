from lib.counter import *

def test_counter_return_correct():
    counter = Counter()
    counter.add(10)
    
    result = counter.report()
    assert result == "Counted to 10 so far."
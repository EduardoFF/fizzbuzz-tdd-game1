from fizzbuzz import fizzBuzz


def tests_numbers():
    assert fizzBuzz(1) == "1"
    assert fizzBuzz(2) == "2"

def test_number_tree():
    assert fizzBuzz(3) == "Fizz"

def test_number_6():
    assert fizzBuzz(6) == "Fizz"

def test_number_7():
    assert fizzBuzz(7) == "Buzz"

def test_number_9():
    assert fizzBuzz(9) == "Fizz"
def test_fizzbuzz():
    assert fizzBuzz(15) == "FizzBuzz"
    assert fizzBuzz(30) == "FizzBuzz"

from fizzbuzz import fizzBuzz


def tests_numbers():
    assert fizzBuzz(1) == "1"
    assert fizzBuzz(2) == "2"

def test_number_tree():
    assert fizzBuzz(3) == "Fizz"

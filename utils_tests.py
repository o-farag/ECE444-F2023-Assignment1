import utils

test_instance = utils.utils

# Test ints
assert test_instance.reversed(301) == 103
assert test_instance.reversed(3) == 3
assert test_instance.reversed(10) == 1
assert test_instance.reversed(122334) == 433221
assert test_instance.reversed(-1) == "invalid input"

assert test_instance.formatter(8)[0] == '0b1000'
assert test_instance.formatter(8)[1] == '0o10'

#Test floats
assert test_instance.reversed(15.5) == "invalid input"
assert test_instance.reversed(0.5) == "invalid input"
assert test_instance.reversed(5.0) == "invalid input"
assert test_instance.reversed(0.0) == "invalid input"
assert test_instance.reversed(-.5) == "invalid input"

assert test_instance.formatter(15.2) == "invalid input"

#Test strings
assert test_instance.reversed("112") == 211
assert test_instance.reversed("0") == 0
assert test_instance.reversed("1a12") == "invalid input"

assert test_instance.formatter("hello") == "invalid input"
assert test_instance.formatter("16")[0] == '0b10000'
assert test_instance.formatter("16")[1] == '0o20'


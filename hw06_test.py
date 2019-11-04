# Brett Roach
# 6907380

from hw06 import num_chars

def test_num_chars_1():
    assert num_chars(["alphabet soup"]) == 13

def test_num_chars_2():
    assert num_chars("four") == -1

def test_num_chars_3():
    assert num_chars(["alphabet", "soup", 7]) == -1

def test_num_chars_4():
    assert num_chars(["alphabet", " ", "soup"]) == 13

from hw06 import compute_factorial

def test_compute_factorial_1():
    assert compute_factorial("cheese") == -1

def test_compute_factorial_2():
    assert compute_factorial(-47) == -1

def test_compute_factorial_3():
    assert compute_factorial(3) == 6

def test_compute_factorial_4():
    assert compute_factorial(10) == 3628800

from hw06 import get_max

def test_get_max_1():
    assert get_max("PB&J") == None

def test_get_max_2():
    assert get_max([1, 2, 3, "four"]) == None

def test_get_max_3():
    assert get_max([0, 1, 2, 3, 4, 5, 4, 3, 2, 25, 1, 0]) == 25

def test_get_max_4():
    assert get_max([1]) == 1

from hw06 import get_index

def test_get_index_1():
    assert get_index("skate", "let's skate!") == None

def test_get_index_2():
    assert get_index("skate", [1, 2, 3, 4]) == -1

def test_get_index_3():
    assert get_index("skate", ["let's", " ", "skate", "!"]) == 2

def test_get_index_4():
    assert get_index(3, [1, 2, 3, 4]) == 2






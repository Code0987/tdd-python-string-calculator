import pytest
import random

from string_calculator import add


def test_empty_string():
    assert add('') == 0


def test_single_number_string():
    assert add('1') == 1


def test_2_comma_seprated_numbers_string():
    assert add('1,5') == 6


def test_3_comma_seprated_numbers_string():
    assert add('1,5,10') == 16


def test_many_comma_seprated_numbers_string():
    many_nums = [i for i in range(1, random.randint(100, 1000))]
    many_nums_sum = sum(many_nums)
    many_nums_str = ','.join(map(str, many_nums))
    assert add(many_nums_str) == many_nums_sum


def test_2_new_line_seprated_numbers_string():
    assert add('1\n5') == 6


def test_many_new_line_seprated_numbers_string():
    many_nums = [i for i in range(1, random.randint(100, 1000))]
    many_nums_sum = sum(many_nums)
    many_nums_str = '\n'.join(map(str, many_nums))
    assert add(many_nums_str) == many_nums_sum


def test_comma_and_new_line_seprated_numbers_string():
    assert add('1\n5,10') == 16


def test_semicolon_delimiter_numbers_string():
    assert add('//;\n1;5') == 6


def test_hash_delimiter_numbers_string():
    assert add('//#\n1#5') == 6


def test_negative_numbers_string_exception():
    with pytest.raises(Exception, match='negatives not allowed -1, -10'):
        add('1,10,-1,-10')

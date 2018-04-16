import pytest
from multi_bracket_validation import multi_bracket_validation


def test_multi_bracket_validation_false(small_false_string):
    """ test for unmatched brackets """
    assert multi_bracket_validation(small_false_string) is False


def test_square_bracket_validation_true(square_true_string):
    """ test for matched brackets """
    assert multi_bracket_validation(square_true_string) is True


def test_mixed_square_bracket_validation_true(mixed_square_true_string):
    """ test for mactched case. The string\
    is consisted of alphabets and brackets.
    """
    assert multi_bracket_validation(mixed_square_true_string) is True


def test_type_error():
    """ test for TypeError when input is number """
    with pytest.raises(TypeError):
        multi_bracket_validation(342512)


def test_two_parenthesis(two_bracket):
    """ test for two parentheses"""
    assert multi_bracket_validation(two_bracket) is True

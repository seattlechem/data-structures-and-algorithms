from multi_bracket_validation import multi_bracket_validation


def test_multi_bracket_validation_false(small_false_string):
    assert multi_bracket_validation(small_false_string) is False


def test_square_bracket_validation_true(square_true_string):
    assert multi_bracket_validation(square_true_string) is False


def test_mixed_square_bracket_validation_true(mixed_square_true_string):
    assert multi_bracket_validation(mixed_square_true_string) is False

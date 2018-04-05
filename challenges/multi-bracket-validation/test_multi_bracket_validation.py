import multi_bracket_validation


def test_multi_bracket_validation_false():
    import pdb; pdb.set_trace()
    small = '[[[[[[['
    assert multi_bracket_validation(small) is False

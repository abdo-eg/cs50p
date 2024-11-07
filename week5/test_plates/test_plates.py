from plates import is_valid


def test_start_letters():
    assert is_valid("ca50") == True
    assert is_valid("a520") == False


def test_length():
    assert is_valid("at44") == True
    assert is_valid("as12345") == False


def test_number_place():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


def test_zero_place():
    assert is_valid("AAA02") == False
    assert is_valid("AAA20") == True


def test_alphanumeric():
    assert is_valid("aaa?=") == False
    assert is_valid("AAA520") == True

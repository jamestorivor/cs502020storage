from vanity import is_valid

def test_valid():
    assert is_valid("CS50") ==True
    assert is_valid("C") == False
    assert is_valid("CS49567") == False
def test_nonalphanum():
    assert is_valid("PI3.45") == False
    assert is_valid("PI 23") == False
def test_0():
    assert is_valid("CS05") == False
from response import validate

def test_proper():
    assert validate("marcus@gmail.com") == "Valid"
    
def test_multiple():
    assert validate("marcus@@@harvard.com") == "Invalid"
    
def test_com():
    assert validate("marcus@gmail..com") == "Invalid"
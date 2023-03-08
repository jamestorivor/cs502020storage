from bank import value

def test_hello():
    assert value("Hello, Newman") == "0"
def test_hey():
    assert value("Hey") == "20"
def test_any():
    assert value("Bye bye") == "100"
from fuel import convert,gauge

def test_convert():
    assert convert("3/4") == 0.75
    assert convert("1/4") == 0.25

def test_gauge():
    assert gauge(.99) == "F"
    assert gauge(.01) == "E"
    assert gauge(.25) == "25%"
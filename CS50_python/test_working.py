from working import convert

def test_hour():
    assert convert("9 AM to 5 PM") == "09 : 00 to 17 : 00"
    
def test_HandM():
    assert convert("9 : 30 AM to 6 : 30 PM") == "09 : 30 to 18 : 30"
    
def test_others():
    assert convert("12 : 00 AM to 10 : 30 PM") == "00 : 00 to 22 : 30"
    assert convert("Not valid") == ValueError
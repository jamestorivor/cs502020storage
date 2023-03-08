from numb3rs import validate

def test_regular():
    assert validate("127.0.0.1") == True
    
def test_outrange():
    assert validate("1.2.3.1000") == False
    
def test_word():
    assert validate("cat") == False
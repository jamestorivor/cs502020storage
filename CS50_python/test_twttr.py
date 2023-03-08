from twttr import shorten

def test_word():
    assert shorten('Hello') == 'Hll'
    
def test_number():
    assert shorten('cs50') == 'cs50'
    
def test_sentence():
    assert shorten('Just Testing 50?') == 'Jst Tstng 50?'

from um import count

def test_normalum():
    assert count("HI, um im going um shopping today um yea") == 3
    
def test_yummy():
    assert count("um yummy hehe") == 1

def test_umothers():
    assert count("um, um? um...") == 3 
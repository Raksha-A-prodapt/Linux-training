from addition import add,sub,mul,div

def test_add_positive_numbers():
    assert add(2,3)==5

def test_add_negative_numbers():
    assert add(-2,-3) ==-5

def test_add_zero():
    assert add(0,5)==5
def test_positive_neagtive():
    assert add(5,-3)==2

def test_float():
    assert add(2.5,3.1)==5.6

def test_sub():
    assert sub(5,3)==2
def test_sub_neg():
    assert sub(-5,-3)==-2

def test_multiply():
    assert mul(2,3)==6

def test_mul_zero():
    assert mul(8,0)==0
def test_div():
    assert div(6,3)==2

def test_div_zero():
    try:
        div(5,0)
    except ZeroDivisionError:
        pass
    else:
        assert False, "Expected ZeroDivisionError"


    
import Area

def test_rect():
    x=5
    y=7
    result=Area.rectangle(x,y)
    assert x*y==result

def test_periRec():
    x=5
    y=8
    result=Area.perimeter_rect(x,y)
    assert 2*(x+y)==result

def test_areaSquare():
    x=8
    result=Area.area_square(x)
    assert x*x==result
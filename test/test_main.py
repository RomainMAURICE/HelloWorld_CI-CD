from app.main import calcul

def test_calcul_true():
    assert calcul(2, 3) == 5

def test_calcul_false():

    assert calcul(10, 10) != 30    

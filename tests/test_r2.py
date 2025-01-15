from matrics_calculator.r2 import r2

def test_r2():
    data = {
    'math_test': [80, 85, 90, 95],
    'science_test': [78, 82, 88, 92],
    'final_grade': [84, 87, 91, 94],
    'absences': [3, 0, 1, 30]
    }
    
    assert r2(1, 0) == None
    
    assert r2([],[1,2,3]) == None
    
    assert r2(data['math_test'], data['final_grade']) == 0.997
    
    assert r2(data['math_test'], data['absences']) == 0.541
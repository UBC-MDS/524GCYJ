from matrics_calculator.r2 import r2

def test_r2_0_input():
    """
    Tests function's output if given 0 as input. Function
    should return None.
    """
    assert r2(1, 0) == None

def test_r2_empty_list():
    """
    Tests function's output if given an empty string as input. 
    Function should return None.
    """
    assert r2([],[1,2,3]) == None
    
def test_r2_calculation_1():
    """
    Tests functions calculation when given two highly correlated
    columns. Function should run correctly and return a high r-squared
    value indicating high correlation.
    """
    data = {
    'math_test': [80, 85, 90, 95],
    'science_test': [78, 82, 88, 92],
    'final_grade': [84, 87, 91, 94],
    'absences': [3, 0, 1, 30]
    }

    assert r2(data['math_test'], data['final_grade']) == 0.997

def test_r2_calculation_2():
    """
    Tests functions calculation when given two uncorrelated
    columns. Function should run correctly and return a low r-squared
    value indicating low correlation.
    """
    data = {
    'math_test': [80, 85, 90, 95],
    'science_test': [78, 82, 88, 92],
    'final_grade': [84, 87, 91, 94],
    'absences': [3, 0, 1, 30]
    }

    assert r2(data['math_test'], data['absences']) == 0.541
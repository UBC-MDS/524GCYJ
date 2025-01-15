import pytest
from matrics_calculator.mae import mae

def test_mean_absolute_error_correct_calculation():
    """
    Test if the function correctly calculates MAE with valid input.
    """
    y_true = [100, 200, 300]
    y_pred = [110, 190, 290]
    result = mean_absolute_error(y_true, y_pred)
    assert result == pytest.approx(10.0, rel=1e-5)


def test_mean_absolute_error_negative_values():
    """
    Test if the function handles negative values correctly.
    """
    y_true = [-1, -2, -3]
    y_pred = [-1, -2, -4]
    result = mean_absolute_error(y_true, y_pred)
    assert result == 1.0

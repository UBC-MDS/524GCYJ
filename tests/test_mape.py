import pytest
from matrics_calculator.MAPE import mean_absolute_percentage_error

# Test case: Standard inputs with valid values
def test_mape_standard_case():
    """
    Test MAPE with typical inputs where both y_true and y_pred are valid,
    numeric, and non-zero. Expect a correct percentage error calculation.
    """
    y_true = [100, 200, 300]
    y_pred = [110, 190, 290]
    result = mean_absolute_percentage_error(y_true, y_pred)
    assert pytest.approx(result, 0.01) == 6.1111


# Test case: Very small positive values in y_true and y_pred
def test_mape_edge_case_small_values():
    """
    Test MAPE with very small positive values in y_true and y_pred.
    Ensures that the function handles small numbers correctly
    without precision errors or underflow.
    """
    y_true = [0.1, 0.2, 0.3]
    y_pred = [0.09, 0.21, 0.31]
    result = mean_absolute_percentage_error(y_true, y_pred)
    assert pytest.approx(result, 0.01) == 6.1111


# Test case: Mismatched lengths of y_true and y_pred
def test_mape_error_mismatched_lengths():
    """
    Test MAPE with mismatched lengths for y_true and y_pred.
    The function should raise a ValueError if the input lengths do not match.
    """
    y_true = [100, 200, 300]
    y_pred = [110, 190]
    with pytest.raises(ValueError, match="must have the same length"):
        mean_absolute_percentage_error(y_true, y_pred)


# Test case: Zero value in y_true
def test_mape_error_zero_in_y_true():
    """
    Test MAPE with y_true containing zero values.
    The function should raise a ValueError to prevent division by zero.
    """
    y_true = [100, 0, 300]
    y_pred = [110, 190, 290]
    with pytest.raises(ValueError, match="contains zero values"):
        mean_absolute_percentage_error(y_true, y_pred)


# Test case: Extreme predictions significantly off from actual values
def test_mape_extreme_predictions():
    """
    Test MAPE with extreme differences between y_true and y_pred.
    Ensures that the function calculates a high MAPE value appropriately.
    """
    y_true = [100, 200, 300]
    y_pred = [200, 100, 600]
    result = mean_absolute_percentage_error(y_true, y_pred)
    assert pytest.approx(result, 0.01) == 83.3333
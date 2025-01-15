from matrics_calculator.MSE import mean_squared_error
import pytest

def test_mean_squared_error():
    """
    Unit tests for the mean_squared_error function.
    These tests ensure the function behaves as expected under different conditions.
    """

    # Test case 1: Basic test
    """
    Test Case 1:
    Verifies the function calculates the correct MSE for a basic input of y_true and y_pred.
    """
    y_true = [3, -0.5, 2, 7]
    y_pred = [2.5, 0.0, 2, 8]
    assert mean_squared_error(y_true, y_pred) == 0.375

    # Test case 2: All predictions are the same as true values
    """
    Test Case 2:
    Verifies the function returns 0 when the predictions perfectly match the true values.
    """
    y_true = [1, 2, 3]
    y_pred = [1, 2, 3]
    assert mean_squared_error(y_true, y_pred) == 0.0

    # Test case 3: Floating-point values
    """
    Test Case 3:
    Verifies the function handles floating-point values correctly and returns approximate results.
    """
    y_true = [1.5, 2.5, 3.5]
    y_pred = [1.0, 2.0, 3.0]
    assert mean_squared_error(y_true, y_pred) == pytest.approx(0.25)

    # Test case 4: Mismatched lengths
    """
    Test Case 4:
    Verifies the function raises a ValueError when the input lists have different lengths.
    """
    y_true = [1, 2, 3]
    y_pred = [1, 2]
    with pytest.raises(ValueError):
        mean_squared_error(y_true, y_pred)

    # Test case 5: Large numbers
    """
    Test Case 5:
    Verifies the function calculates the correct MSE for large input values.
    """
    y_true = [1000, 2000, 3000]
    y_pred = [1100, 1900, 3100]
    assert mean_squared_error(y_true, y_pred) == 10000.0

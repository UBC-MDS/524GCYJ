import pytest
from matrics_calculator.MAE import mean_absolute_error

def test_mean_absolute_error_type_error():
    """
    Test if the function raises a TypeError when inputs are not array-like.
    """
    with pytest.raises(TypeError, match="y_true and y_pred must be array-like"):
        mean_absolute_error(123, [1, 2, 3])
    with pytest.raises(TypeError, match="y_true and y_pred must be array-like"):
        mean_absolute_error([1, 2, 3], "not an array")

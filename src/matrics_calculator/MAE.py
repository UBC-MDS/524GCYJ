# Mean Absolute Error (MAE) calculation
def mean_absolute_error(y_true, y_pred):
 """
    Calculate the Mean Absolute Error (MAE) metric for regression.

    This function computes the average absolute difference between the predicted values (`y_pred`) 
    and the actual values (`y_true`). It measures the magnitude of errors in prediction, providing 
    a straightforward evaluation of a model's accuracy.

    Parameters:
    ----------
    y_true : array-like
        True values of the target variable.
    y_pred : array-like
        Predicted values from the model.

    Returns:
    -------
    float
        The Mean Absolute Error.
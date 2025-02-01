
# Mean Squared Error (MSE) calculation
def mean_squared_error(y_true, y_pred): 
    """
    Calculate the Mean Squared Error (MSE) between actual and predicted values.

    This function computes the average squared difference between the predicted values (`y_pred`)
    and the actual values (`y_true`). It is commonly used as a metric to evaluate regression models.
    
    Parameters
    ----------
    y_true : list or array-like
        The actual observed values.
    y_pred : list or array-like
        The predicted values from the model.

    Returns
    -------
    float
        The Mean Squared Error (MSE) value, which is non-negative. 
        A smaller value indicates that the predictions are closer to the actual values.

    Notes
    -----
    MSE is defined as:
        MSE = (1 / n) * sum((y_true - y_pred)²)
    where `n` is the number of observations.
    
    This function assumes that the input `y_true` and `y_pred` have the same length.

    Examples
    --------
    >>> y_true = [3, -0.5, 2, 7]
    >>> y_pred = [2.5, 0.0, 2, 8]
    >>> mean_squared_error(y_true, y_pred)
    0.375
    """
    # Ensure the input lists have the same length; otherwise, raise an error
    if len(y_true) != len(y_pred):
        raise ValueError("The lengths of y_true and y_pred must be the same.")
        
    # Compute the squared differences between actual and predicted values, sum them, 
    # and divide by the total number of observations to calculate MSE
    mse = sum((true - pred) ** 2 for true, pred in zip(y_true, y_pred)) / len(y_true)
    return mse


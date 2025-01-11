# r-squared value calcualtion
def r2(df, predictor, response): 
    """
    Calculates r-squared using linear regression.

    Computes the r-squared value (coefficient of determination) using the provided dataframe,
    predictor column names, and response column name.
    
    Parameters
    ----------
    df : dataframe
        Dataframe containing necessary predictor values and response value.
    predictor : list or string
        Predictor values to be used in calculating r-sqaured value.
    response : list or string
        Response values to be used in calculating r-sqaured value.

    Returns
    -------
    float
        r-sqaured value which is <= 1. 1 is the best score and a score below 0 is worse than 
        using the mean of the target as predictions.

    Examples
    --------
    >>> r2(student_grades, math_test, final_grade)
    0.88
    >>> r2(student_grades, [math_test, science_test], absences)
    -0.32
    """


def mae_baseline(dataframe, target_col):
    from sklearn.metrics import mean_absolute_error

    guess = dataframe[target_col].mean()
    y_pred = [guess] * len(dataframe[target_col])
    baseline_mae = mean_absolute_error(dataframe[target_col], y_pred)

    return baseline_mae

def accuracy_baseline(dataframe, target_col):
    from sklearn.metrics import accuracy_score
    majority_class = dataframe[target_col].mode()[0]
    y_pred = [majority_class] * len(dataframe[target_col])

    return accuracy_score(dataframe[target_col], y_pred)




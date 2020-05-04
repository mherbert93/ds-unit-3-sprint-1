def mae_baseline(dataframe, target_col):
    from sklearn.metrics import mean_absolute_error
    target = 'total_cases'

    guess = dataframe[target_col].mean()
    y_pred = [guess] * len(dataframe[target_col])
    baseline_mae = mean_absolute_error(dataframe[target_col], y_pred)

    return "Baseline MAE is: " + str(baseline_mae)




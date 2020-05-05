class Baseline:
    def __init__(self, dataframe, target):
        self.dataframe = dataframe
        self.target = target

    def mae(self):
        """
        Used to calculate a MAE baseline based on the mean.

        Parameters
        ----------
        dataframe: Expects pandas.DataFrame

        Returns
        -------
        Float
        """
        from sklearn.metrics import mean_absolute_error

        guess = self.dataframe[self.target].mean()
        y_pred = [guess] * len(self.dataframe[self.target])
        baseline_mae = mean_absolute_error(self.dataframe[self.target], y_pred)

        return baseline_mae

    def accuracy(self):
        """
        Used to calculate an accuracy baseline based on the majority class.

        Parameters
        ----------
        dataframe: Expects pandas.DataFrame

        Returns
        -------
        Float
        """
        from sklearn.metrics import accuracy_score
        majority_class = self.dataframe[self.target].mode()[0]
        y_pred = [majority_class] * len(self.dataframe[self.target])

        return accuracy_score(self.dataframe[self.target], y_pred)

if __name__ == "__main__":
    import pandas as pd
    df = pd.DataFrame({'target': ['True', 'True', 'True', 'True', 'False'], 'feature1': [5, 6, 4, 5, 5]})
    baseline = Baseline(dataframe=df, target='target')
    print("Baseline accuracy is: ", baseline.accuracy())

    df = pd.DataFrame({'target': [250, 300, 225, 400, 600], 'feature1': [2, 3, 2, 5, 7]})
    baseline = Baseline(dataframe=df, target='target')
    print("Baseline MAE is: ", baseline.mae())




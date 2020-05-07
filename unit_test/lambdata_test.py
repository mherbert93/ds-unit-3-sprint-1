import unittest
from lambdata.lambdata_mherbert93 import Baseline

class TestMyPackage(unittest.TestCase):

    def test_accuracy(self):
        import pandas as pd
        df = pd.DataFrame({'target': ['True', 'True', 'True', 'True', 'False'], 'feature1': [5, 6, 4, 5, 5]})
        baseline = Baseline(dataframe=df, target='target')
        self.assertEqual(baseline.accuracy(), 0.8)

    def test_mae(self):
        import pandas as pd
        df = pd.DataFrame({'target': [250, 300, 225, 400, 600], 'feature1': [2, 3, 2, 5, 7]})
        baseline = Baseline(dataframe=df, target='target')
        self.assertEqual(baseline.mae(), 116.0)

if __name__ == "__main__":
    unittest.main()
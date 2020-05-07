# ds-unit-3-sprint-1

The purpose of this package is to have an easy way to quickly calculate a baseline for a predictive model.

For classification, the baseline is calculated from the majority class. 

For regression, the baseline is calculated from the mean.

### Installing

pip install -i https://test.pypi.org/simple/ lambdata-mherbert93

### Examples

baseline = Baseline(df, targetcol)
baseline.accuracy()
baseline.mae()





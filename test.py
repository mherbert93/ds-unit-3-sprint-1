#%%

from lambdata_mherbert93 import mae_baseline
import pandas

df = pandas.DataFrame({"prices": [225, 250, 235, 500, 600], "feature1": [5, 6, 5, 10, 12], "feature2": [35, 37, 35, 60, 65]})

print(df.head())
#%%

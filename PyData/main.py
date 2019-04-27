import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = sn.load_dataset('iris')
#print(df.head())
#print(df.describe())

sn.distplot(df.sepal_length, bins=20, kde=True, rug=True)
plt.show()
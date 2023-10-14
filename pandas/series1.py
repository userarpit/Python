import pandas as pd
import numpy as np

arr = np.arange(3)
s = pd.Series(arr, index=[100, 101, 102])
print(s)

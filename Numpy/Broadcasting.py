import numpy as np

np_arr = np.array([[2,3],[4,10]])
np_arr_broad = np_arr *5
print(np_arr_broad)

np_five = np.array([[5,6],[7,8]])
np_arr_nobroad = np_arr * np_five
print(np_arr_nobroad)

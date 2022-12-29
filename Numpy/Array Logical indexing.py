import numpy as np

my_list = [[1,5,3],[4,1,6],[2,4,10]]

np_array = np.array(my_list)
np_cond = np_array [np_array > 3]
print(np_cond)
print(np_array > 3)
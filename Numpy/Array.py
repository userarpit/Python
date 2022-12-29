import numpy as np
import test

my_list = [1,2,3]

my_array = np.asarray(my_list)

print(type(my_array))
print(my_array)
print(my_array.dtype)
print(my_array.shape)

np_zeroes = np.zeros((5,5),dtype=int)
print(np_zeroes)

np_ones = np.ones((5,5),dtype=int)
print(np_ones)

np_range = np.arange(start = 2, step = 2, stop = 20)
print(np_range)

np_linspace = np.linspace (start = 2, stop=20, num = 5)
print(np_linspace)

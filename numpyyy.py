import numpy as np

arr = np.zeros((10,10))
arr = np.full((4,5), 78)
arr1 = np.arange(45)
arr2 = np.arange(25, 70)
arr3 = np.arange(50, 95)
arr = np.column_stack((arr1, arr2, arr3))
# commom
arr = np.intersect1d(arr2, arr3)
# unique
arr = np.setdiff1d(arr2, arr3)
arr = np.setdiff1d(arr3, arr2)
arr = np.sum([arr1, arr2, arr3], axis=1) # axis 0 for col and 1 for row
arr = arr2 + 100
arr = arr3 * 2
arr = arr1 / 5
arr = np.sum([arr1, arr2]) - np.sum(arr3)
arr_rand = np.random.randint(34, 100, 15)
# print(arr_rand)
arr = np.mean(arr_rand)
arr = np.median(arr_rand)
arr = np.std(arr_rand)
# np.save('saved', np.arange(10_00_000))
# arr = np.load('saved.npy') # use with full fil name and extention nname

print(arr)
# print(type(arr[0]))

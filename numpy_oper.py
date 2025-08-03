import numpy as np


arr1 = np.array([4, 5, 6, 8])
arr2 = np.array([7, 8, 1, 2])

arr_sum = arr1 + arr2
arr_product = arr1 * arr2

arr_mean = np.mean(arr1)
arr_max = np.max(arr1)
arr_min = np.min(arr1)
arr_median = np.median(arr1)
arr_var = np.var(arr1)
arr_std = np.std(arr1)
arr_reshape = arr1.reshape(2, 2)
arr_split = np.split(arr1 , 2)
arr_concat = np.concatenate([arr1, arr2])
arr_reverse = arr1[::-1]


print("arr1 : ", arr1)
print("arr2 : ", arr2)
print("Sum of arr1 and arr2 : ",arr_sum)
print("Product of arr1 and arr2 : ", arr_product)
print("Mean value of arr1 : ", arr_mean)
print("Max value of arr1 : ", arr_max)
print("Min value of arr2 : ", arr_min)
print("Median value of arr1 : ", arr_median)
print("Variance of arr1 : ", arr_var)
print("Standard Deviation of arr1 : ", arr_std)
print("Reshape of arr1 : ", arr_reshape)
print("Split of arr1 : ", arr_split)

print("Concatenate of arr1 and arr2 : ", arr_concat)
print("Reverse of arr1 : ",arr_reverse)



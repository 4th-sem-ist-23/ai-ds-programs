import numpy as np


# Slicing of 1D array
oned_arr = np.array([23, 45, 68, 98, 12])

print("1D Array : ") 
print(oned_arr)
print("Slicing : ")
print(oned_arr[0:2])
print()

# Slicing of 2D array
twod_arr = np.array([
	[43, 12, 23],
	[7, 9, 10]
])

print("2D Array : ") 
print(twod_arr)
print("Slicing : ")
print(twod_arr[0][0:2])
print()

# Slicing of 3D array

threed_arr = np.array([
	[
		[45, 32, 12],
		[12, 7, 9]
	],
	[
		[5, 12, 4],
		[12, 9, 10]
	]
])

print("3D Array : ") 
print(threed_arr)
print("Slicing : ")
print(threed_arr[0][0][0:2])
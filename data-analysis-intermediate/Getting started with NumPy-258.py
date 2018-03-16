## 2. Creating arrays ##

import numpy as np
vector = np.array([10,20,30])
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

## 3. Array shape ##

import numpy as np
vector = np.array([10, 20, 30])
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
vector_shape = vector.shape
matrix_shape = matrix.shape
print(vector_shape, matrix_shape)

## 4. Using NumPy ##

import numpy as np
world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',')
print(type(world_alcohol))

## 5. Data types ##

world_alcohol_dtype = world_alcohol.dtype
print(world_alcohol_dtype)

## 7. Reading in the data correctly ##

import numpy as np
world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter = ',', dtype='U75', skip_header = 1)
print(world_alcohol)

## 8. Indexing arrays ##

uruguay_other_1986 = world_alcohol[1,4]
third_country = world_alcohol[2]

## 9. Slicing arrays ##

countries = world_alcohol[:,2]
alcohol_consumption = world_alcohol[:,4]

## 10. Slicing one dimension ##

first_two_columns = world_alcohol[:, :2]
first_ten_years = world_alcohol[:10, 0]
first_ten_rows = world_alcohol[:10, :]

## 11. Slicing arrays ##

first_twenty_regions = world_alcohol[:20, 1:3]
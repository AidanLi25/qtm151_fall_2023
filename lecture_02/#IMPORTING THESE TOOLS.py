#IMPORTING THESE TOOLS
import numpy as np
import matplotlib as plt
import pandas as pd

#READING GRAPHS
carfeatures = pd.read_csv('data/features.csv')

#ASSIGNING VARIABLE TYPES
#finding variable type
type(3) #int
type("i love weiwei") #str
type(3.4) #float
#assign variables with =
number5 = 5
#only str + str and int + int
name = str(5)
"Amnesiac is Radiohead's album number " + " " + name

#LISTS
list_radioheadalbums = ["Ok Computer", "Kid A", "The Bends"]
list_x = [1, 2, 3, 4]
list_xsquared = [2, 4, 9, 16]
plt.scatter(x = list_x, y = list_xsquared)
plt.xlabel("Values")
plt.ylabel("Values Squared")
plt.show()

#Mathematical Operations
print(np.log(1))
print(np.exp(1))
print(np.sin(1))
print(np.cos(1))
print(np.sqrt(1))
x = 5 
print((1/np.sqrt(2*np.pi))*(np.exp(-x**2)))

#Arrays
vec_a = np.array([1, 2, 3, 4])
vec_b = np.array([5, 6 , 7, 8])
print(vec_a[0])
print(vec_a * 2)
print(vec_a + vec_b)
print(np.mean(vec_a))





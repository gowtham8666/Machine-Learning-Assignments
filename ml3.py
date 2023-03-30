#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
# Creating random vector of size 15 with integers in range 1-20
arr1 = np.random.randint(1, 21, size=15)
# Reshaping the array to 3 by 5
arr1 = arr1.reshape(3, 5)
# Printing array shape
print(arr1.shape)
# Replace the max in each row by 0
arr1[np.arange(3), np.argmax(arr1, axis=1)] = 0
print(arr1)


# In[5]:


import numpy as np
# Creating 2D array of size 4x3 with 4-byte integer elements
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=np.int32)
# Printing array shape, type, and data type
print("Array shape:", arr1.shape)
print("Array type:", type(arr1))
print("Array data type:", arr1.dtype)



# In[6]:


arr2 = np.array([[3, -2], [1, 0]])
eigenval, eigenvect = np.linalg.eig(arr2)
print("Eigenvalues:", eigenval)
print("Right eigenvectors:")
print(eigenvect)


# In[7]:


arr3 = np.array([[0, 1, 2], [3, 4, 5]])
diag_sum = np.trace(arr3)
print("Diagonal sum:", diag_sum)


# In[10]:


arr4 = np.array([[1, 2], [3, 4], [5, 6]])
reshaped_arr4 = arr4.reshape((2, 3))
print("Reshaped 3x2 array:")
print(reshaped_arr4)
#Reshape 2x3:
arr5 = np.array([[1, 2, 3], [4, 5, 6]])
reshaped_arr5 = arr5.reshape((3, 2))
print("Reshaped 2x3 array:")
print(reshaped_arr5)



# In[12]:


import matplotlib.pyplot as plt
# Given sample data
lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# Creating a pie chart
plt.pie(popularity, labels=lang, autopct='%1.1f%%')
# Title of pie chart
plt.title('Popularity of Programming Languages')
# To show the plot
plt.show()


# In[ ]:







# In[1]:


rows = input("Enter the height of pyramid")
rows = int (rows)
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")


# In[2]:


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("The elements at odd places are : ")
for i in range(1, len(my_list), 2):
   print(my_list[i])


# In[3]:


s = [23, 'Python',23.98]
x = []
for i in range(len(s)):
    x.append(type(s[i]))
print(s)
print(x)


# In[4]:


def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5]))


# In[5]:


def up_low(string):
  uppers = 0
  lowers = 0
  for char in string:
    if char.islower():
      lowers += 1
    elif char.isupper():
      uppers +=1
  return(uppers, lowers)

print(up_low('Welcome to Machine Learning'))


# In[ ]:





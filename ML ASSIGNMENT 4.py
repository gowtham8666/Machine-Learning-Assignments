#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.pandas
import pandas as pd
#Read the csv file
data = pd.read_csv("data.csv")
data.head()


# In[3]:


#shows statastical description of data
data.describe()


# In[4]:


#Check if the data has null values
data.isnull().any()


# In[5]:


#Replace the null values with the mean
data.fillna(data.mean(), inplace=True)
data.isnull().any()


# In[6]:


#Select at least two columns and aggregate the data using: min, max, count, mean
data.agg({'Maxpulse':['min','max','count','mean'],'Calories':['min','max','count','mean']})


# In[7]:


#Filter the dataframe to select the rows with calories values between 500 and 1000.
data.loc[(data['Calories']>500)&(data['Calories']<1000)]


# In[30]:


#Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
data.loc[(data['Calories']>500)&(data['Pulse']<100)]


# In[33]:


#Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”
df_modified = data[['Duration','Pulse','Calories']]
df_modified.head()


# In[ ]:


#Delete the “Maxpulse” column from the main df dataframe
del data['Maxpulse']


# In[11]:


data.head()


# In[13]:


data.dtypes


# In[14]:


import numpy as np

data['Calories'] = data['Calories'].astype(np.int64)
data.dtypes


# In[15]:


#Using pandas create a scatter plot for the two columns (Duration and Calories).
data.plot.scatter(x='Duration',y='Calories',c='DarkBlue')


# In[16]:


#1.Titanic dataset
import pandas as pd
import seaborn as sns
from sklearn import preprocessing
import matplotlib.pyplot as plt

df=pd.read_csv("train.csv")
df.head()


# In[17]:


#correlation between ‘survived’ (target column) and ‘sex’ column for the Titanic use case in class.
le = preprocessing.LabelEncoder()
df['Sex'] = le.fit_transform(df.Sex.values)
df['Survived'].corr(df['Sex'])


# In[18]:


# Drop non-numeric columns from the dataframe
df = df.drop(['Name', 'Sex','Ticket','Cabin','Embarked'], axis=1)

#creating corelation matrix
matrix = df.corr()
print(matrix)


# In[19]:


#visualization 1 of Titanic Dataset
df.corr().style.background_gradient(cmap="Greens")


# In[20]:


#visualization 2 of Titanic Dataset
sns.heatmap(matrix, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag')
plt.show()


# In[21]:


#Naïve Bayes method of Titanic Dataset
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer

# Load the dataset
df = pd.read_csv("train.csv")

# Select features and target
features = ['Age', 'Embarked', 'Fare', 'Parch', 'Pclass', 'Sex', 'SibSp']
target = 'Survived'

# Preprocess categorical variables
df['Sex'] = df['Sex'].replace(["female", "male"], [0, 1])
df['Embarked'] = df['Embarked'].replace(['S', 'C', 'Q'], [1, 2, 3])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

# Impute missing values with the mean
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# Train the Naive Bayes model
model = GaussianNB()
model.fit(X_train_imputed, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_imputed)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy * 100))



# In[22]:


#2.Glass Dataset
glass=pd.read_csv("glass.csv")
glass.head()


# In[23]:


#visualization 1 of Glass Dataset
glass.corr().style.background_gradient(cmap="Greens")


# In[24]:


#visualization 2 of Glass Dataset
sns.heatmap(matrix, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag')
plt.show()


# In[25]:


#Naïve Bayes method of Glass Dataset
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

# Load the dataset
glass_data = pd.read_csv('glass.csv')

# Separate the target variable
X = glass_data.drop(['Type'], axis=1)
y = glass_data['Type']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
score = model.score(X_test, y_test)
report = classification_report(y_test, y_pred)

print("Accuracy Score: {:.2f}%".format(score * 100))
print("\nClassification Report:\n", report)


# In[26]:


#Linear SVM method of Glass Dataset
import warnings
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
#To avoid warnings
warnings.filterwarnings("ignore")

# Load the dataset
glass_data = pd.read_csv('glass.csv')

# Separate the target variable
X = glass_data.drop(['Type'], axis=1)
y = glass_data['Type']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear SVM model
model = LinearSVC(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
score = model.score(X_test, y_test)
report = classification_report(y_test, y_pred)

print("Accuracy Score: {:.2f}%".format(score * 100))
print("\nClassification Report:\n", report)


# In[ ]:





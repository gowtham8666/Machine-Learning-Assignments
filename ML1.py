#!/usr/bin/env python
# coding: utf-8



# Q1
import statistics 
age_list = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sorts age list in ascending order by default
age_list.sort()
print ("Sorted list:", age_list) # Displays sorted values
# Displays min value as we used min() method
print ("Min_age:", min(age_list)) 
# Displays max value as we used max() methods
print ("Max_age:", max(age_list)) 
# Adding  min_age and max_age values to the list
age_list.append(min(age_list)) 
age_list.append(max(age_list))
print ("After adding min_age and max_age values again:",age_list) #Displays the list again with new values
# Median (one middle item or two middle items divided by two, as we imported statistics library it 
#calculates easily and provides the output) 
median = statistics.median(age_list)
print ("Median:", median)
# Average age
average= sum(age_list)/len(age_list)
print ("Avg = ", average)
# Range
range=max(age_list)-min(age_list)
print ("Range = ", range)




# Q2
# Create an empty dictionary called dog
dog = dict()
# Adding data to dog dictionarys
dog['name'] = 'TONY'
dog['color'] = 'WHITE'
dog['breed'] = 'PUG'
dog['legs'] = 4
dog['age'] = 4
print("dog dictionary : ", dog)
# creating student dictionary with data
student = {
    "first_name": "GOWTHAM",
    "last_name": "PALURI",
    "gender": "MALE",
    "age": 23,
    "marital status": "single",
    "skills": ["python", "machine learning"],
    "country": "United States",
    "city": "lees summit",
    "address": "OVERLANDPARK"
}
print("student dictionary : ", student)
# length of the student dictionary
len_student = len(student)
# skills of the student from the dictionary
skills = student['skills']
# type of skills
print("type of skills :",type(skills))
# updating student skills
student['skills'].extend(["Java"])
print("updated student skills : ", student["skills"])
student['skills'].extend(["C#"])
print("updated student skills : ", student["skills"])
# keys of student dictionary
print("keys of student dictionary : ", list(student.keys()))
# values of student dictionary
print("values of student dictionary : ", list(student.values()))




# Q3
# creating a tuple for brothers
brothers = ("KLAUS","ELIJAH")
print("brothers : ", brothers)
# creating a tuple for sisters
sisters =  ("FREYA","REBECCA")
print("sisters : ", sisters)

# creating a siblings tuple by adding brothers and sisters
siblings = brothers + sisters
print("siblings : ", siblings)

# length of siblings tuple
length_of_siblings = len(siblings)
print("length of siblings tuple", length_of_siblings)

# adding parents to siblings tuple  to create new tuple
family = siblings + ("MICHAEL","ESTHER")
print("family : ", family)




# Q4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# length of it_companies set
print("length of it_companies set : ", len(it_companies))
# adding twitter company to it_companies
it_companies.add("Twitter")
# removing company from it_companies
it_companies.discard("Oracle")
print("it companies : ", it_companies)
print(""" remove vs discard : 
remove deletes the element from the list if not present it returns Key error, 
discard deletes the element from the list otherwise return None""")
# joining A and B sets
print("Join of A and B : ", A.union(B))
# intersection of A and B sets
print("Intersection of A and B : ",A.intersection(B))
# checking if A is subset of B
print("Is A subset of B : ", A.issubset(B))
# check if A is disjoint of B
print("Is A disjoint of B : ", A.isdisjoint(B))
# A union B and B union A
print("A union B : ", A.union(B))
print("B union A : ", B.union(A))
# symmetric difference between two sets
print("set A difference with set B : ",A.difference(B))
# deleting sets A and B
A.clear()
B.clear()
# converting age list to set
set_ages = set(age)
# comparing length of list and length of set
print("Is length of age list same of length of age set : ", len(age) == len(set_ages))




# Q5
# The radius of a circle is 30 meters.
# radius r
r = 30
# pi value constant
pi = 3.14
# calculating area of circle
_area_of_circle_ =  pi * r * r
print("Area of circle :", _area_of_circle_)
# calculating cirumference of circle
_circum_of_circle_ = 2 * pi * r
print("Circumference of circle :", _circum_of_circle_)

# input from user
r = float(input("Enter radius of circle : "))
# calculating area of circle from user inputs
area_of_circle = pi * r * r
print("Area of circle : ", area_of_circle)




# Q6
sentence = """I am a teacher and I love to inspire and teach people"""
# splitting sentence into words
split_sentence = sentence.split()
print("words : ", split_sentence)
# getting unique words using set
unique_words = set(split_sentence)
print("unique words : ", unique_words)




# Q7
# By using a tab escape sequence we get the following lines.
a= "Name\t Age\tCountry\tCity\t\nAsabeneh 250\tFinland\tHelsinki"
print(a)





# Q8
radius = 10
area = 3.14 * radius ** 2
# print string using format
sent = "The area of a circle with radius {} is {} meters square.".format(radius, area)
print(sent)

#Q9


# input number of students
N = int(input("Enter Number of students : "))
# lb to kg conversion value
lbs_to_kg_convertion_value = 0.4536
lbs = []
kg = []
# input weights of all students
for i in range(0,N):
    lbs.append(int(input("Enter student Weight(lbs) : ")))

print("weight in lbs : ",lbs)

# converte weights to kg
for weight in lbs:
    kg.append(round(weight * lbs_to_kg_convertion_value,2))

print("kg_weights : ", kg)





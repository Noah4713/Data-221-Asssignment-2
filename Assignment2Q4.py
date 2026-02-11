#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas
data=  pandas.read_csv("student.csv")

mylist=[]
for i in data.index:   # loop over rows
    if data.loc[i, "internet"] == 1: #check if internet=1
        mylist.append(i)
studytimelist=[]
for i in data.index:   # loop over rows
    if data.loc[i, "studytime"] >=3: #make sure study time is atleast 3
        studytimelist.append(i)
absenceslist=[]
for i in data.index:   # loop over rows
    if data.loc[i, "absences"] <=5: #make sure absences is no greater than 5
       absenceslist.append(i)

filtered=[]
for i in data.index:
    if i in mylist and i in studytimelist and i in absenceslist: # only append the entries that make all 3 requirements
        filtered.append(i)

filtered_data = data.loc[filtered]

# Save to CSV
filtered_data.to_csv("high_engagement.csv", index=False)

# Number of students
num_students = len(filtered_data)

# Average grade 
avg_grade = filtered_data["grade"].mean()

print("Number of students saved:", num_students)
print("Average grade:", avg_grade)


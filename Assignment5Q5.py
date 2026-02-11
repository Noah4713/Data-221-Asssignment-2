#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

# Load the dataset
data = pd.read_csv("student.csv")

# Create the grade_band column
def assign_grade_band(grade):
    if grade <= 9:
        return "Low"
    elif grade <=14:
        return "Medium"
    else:
        return "High"

data["grade_band"] = data["grade"].apply(assign_grade_band)


summary_table = data.groupby("grade_band").agg(
    num_students=("grade", "count"),
    avg_absences=("absences", "mean"),
    percent_internet=("internet", "mean")  # mean of 0/1 column gives fraction
)

# Convert fraction to percentage
summary_table["percent_internet"] = summary_table["percent_internet"] * 100

# Save the table to CSV
summary_table.to_csv("student_bands.csv")

# Display the summary
print(summary_table)


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

# Load the dataset
data = pd.read_csv("crime.csv")

# Create the 'risk' column based on ViolentCrimesPerPop
data["risk"] = ""
for i in data.index:
    if data.loc[i, "ViolentCrimesPerPop"] >= 0.50:
        data.loc[i, "risk"] = "HighCrime"
    else:
        data.loc[i, "risk"] = "LowCrime"
avg_unemployment = data.groupby("risk")["PctUnemployed"].mean()

# Print results clearly
print("Average unemployment rates by crime risk:")
for risk_level, avg in avg_unemployment.items():
    print(f"{risk_level}: {avg:.2f}%")


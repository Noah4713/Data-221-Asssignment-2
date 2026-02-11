#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Get the main content div
content_div = soup.find("div", id="mw-content-text")
tables = content_div.find_all("table")
target_table = None

# Locate first table with at least 3 data rows
for table in tables:
    rows = table.find_all("tr")
    data_rows = [row for row in rows if row.find_all("td")]
    if len(data_rows) >= 3:
        target_table = table
        break

if target_table is None:
    print("No table with at least 3 data rows was found.")
else:
    # Extract headers if present
    header_cells = target_table.find_all("th")
    if header_cells:
        headers = [cell.get_text(strip=True) for cell in header_cells]
    else:
        # Create default headers if none found
        max_cols = max(len(row.find_all(["td", "th"])) for row in target_table.find_all("tr"))
        headers = [f"col{i+1}" for i in range(max_cols)]

    # Extract all rows
    table_data = []
    for row in target_table.find_all("tr"):
        cells = row.find_all(["td", "th"])
        row_data = [cell.get_text(strip=True) for cell in cells]
        # Pad row if it has fewer columns than headers
        while len(row_data) < len(headers):
            row_data.append("")
        table_data.append(row_data)

    # Save to CSV
    df = pd.DataFrame(table_data[1:] if header_cells else table_data, columns=headers)
    df.to_csv("wiki_table.csv", index=False)
    print(f"Table saved to wiki_table.csv with {len(df)} rows.")


# In[ ]:





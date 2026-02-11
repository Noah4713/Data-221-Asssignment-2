#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Data_science"
headers = {
    "User-Agent": "Mozilla/5.0 (educational scraping example)"
}
# Fetch the page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


# Get the main content div
content_div = soup.find("div", id="mw-content-text")
headings = []

# Extract all h2 tags in the main content
headings = []

# Loop through all h2 tags inside the main content
for h2 in content_div.find_all("h2"):
    # Get the text inside the heading and remove extra spaces
    heading_text = h2.get_text(strip=True)

    # Remove the '[edit]' text if it exists
    heading_text = heading_text.replace("[edit]", "")

    # Skip headings we don't want
    if "References" in heading_text:
        continue
    if "External links" in heading_text:
        continue
    if "See also" in heading_text:
        continue
    if "Notes" in heading_text:
        continue

    # Add the cleaned heading to our list
    headings.append(heading_text)

# Save all headings to a text file, one per line
with open("headings.txt", "w", encoding="utf-8") as f:
    for heading in headings:
        f.write(heading + "\n")

for h in headings:
    print(h)



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

# Print page title
print("Page Title:", soup.title.text)

# Get the main content div
content_div = soup.find("div", id="mw-content-text")

# Find the first paragraph with at least 50 characters
for p in content_div.find_all("p"):
    text = p.get_text(strip=True)
    if len(text) >= 50:
        print("\nFirst Paragraph:\n", text)
        break


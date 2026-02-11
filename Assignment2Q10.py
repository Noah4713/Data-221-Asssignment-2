#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_lines_containing(filename, keyword):
    # List to store first 3 matching lines
    mylist = []
    # Counter for total matching lines
    number_of_matching_lines = 0

    # Open the file and read all lines
    with open(filename, "r") as file:
        content = file.read().splitlines()

    # Loop through each line with line numbers starting at 1
    for count, line in enumerate(content, start=1):
        # Check if keyword appears in the line (case-insensitive)
        if keyword.lower() in line.lower():
            number_of_matching_lines += 1
            # Store only the first 3 matches
            if len(mylist) < 3:
                mylist.append((count, line))

    # Return the first 3 matches and a summary string
    return mylist, f"there are {number_of_matching_lines} lines with the keyword '{keyword}'"

# Test the function with 'lorem'
lines, summary = find_lines_containing("sample-file.txt", "lorem")

# Print the first 3 matching lines
print("First 3 matching lines:")
for line_num, line_text in lines:
    print(f"Line {line_num}: {line_text}")

# Print total number of matching lines
print(summary)


# In[ ]:





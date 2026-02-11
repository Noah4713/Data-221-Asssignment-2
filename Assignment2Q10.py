#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def find_lines_containing(filename, keyword):
    mylist = []
    number_of_matching_lines = 0

    # Open the file
    with open(filename, "r") as file:
        content = file.read().splitlines()

    # Loop through each line with line numbers
    for count, line in enumerate(content, start=1):
        if keyword in line:
            number_of_matching_lines += 1
            if len(mylist) < 3:  # only store first 3 matches
                mylist.append((count, line))

    return mylist, f"there are {number_of_matching_lines} lines with the keyword '{keyword}'"

# Test the function
lines, summary = find_lines_containing("sample-file.txt", "lorem")
print("First 3 matching lines:")
for line_num, line_text in lines:
    print(f"Line {line_num}: {line_text}")

print(summary)


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# open the file and read lines
file = open('sample-file.txt', 'r')
content = file.read().splitlines()  # read all lines and split into a list
file.close()  # close the file

# lists of capital and lowercase letters
capital_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase_Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# list to store normalized lines
normalized_lines = []

# dictionary to map normalized line
line_map = {}

# loop through each line with its line number
for line_number, line in enumerate(content, start=1):
    lowercasecontent = ""  # store lowercase version of line
    for char in line:
        if char in capital_letters:  # if uppercase, convert to lowercase
            index = capital_letters.index(char)
            lowercasecontent += lowercase_Letters[index]
        else:
            lowercasecontent += char  # keep lowercase letters as they are

    no_punctuation_content = ""  # remove non-letter characters
    for char in lowercasecontent:
        if char in lowercase_Letters:  # only keep letters
            no_punctuation_content += char

    normalized_lines.append(no_punctuation_content)  # store normalized line

    # add normalized line to dictionary with its line number and original line
    if no_punctuation_content:  #ignore empty lines
        if no_punctuation_content in line_map:
            line_map[no_punctuation_content].append((line_number, line))
        else:
            line_map[no_punctuation_content] = [(line_number, line)]

# list to store near-duplicate sets
near_duplicates = []
for lines in line_map.values():
    if len(lines) > 1:  # only include lines that appear more than once
        near_duplicates.append(lines)

# print number of near-duplicate sets
print("Number of near-duplicate sets:", len(near_duplicates))
print()

# print first 2 near-duplicate sets
for i in range(min(2, len(near_duplicates))):
    print("Set", i+1)
    for line_num, orig_line in near_duplicates[i]:
        print("  Line", line_num, ":", orig_line)
    print()


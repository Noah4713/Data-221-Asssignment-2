#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 1: Word frequency from sample-file.txt

# open file
file = open("sample-file.txt", "r")
content = file.read()
file.close()

# lists for manual lowercase handling
capital_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                   "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                     "n","o","p","q","r","s","t","u","v","w","x","y","z"]

# convert to lowercase
lowercasecontent = ""
for char in content:
    if char in capital_letters:
        lowercasecontent += lowercase_letters[capital_letters.index(char)]
    else:
        lowercasecontent += char

# remove punctuation from beginning/end of tokens
clean_text = ""
for char in lowercasecontent:
    if char in lowercase_letters or char == " ":
        clean_text += char

# split into words
words = clean_text.split()

# keep only words with at least 2 alphabetic characters
clean_words = []
for word in words:
    letter_count = 0
    for c in word:
        if c in lowercase_letters:
            letter_count += 1
    if letter_count >= 2:
        clean_words.append(word)

# count word frequencies
word_count = {}
for word in clean_words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# manually sort by frequency
sorted_words = []
while word_count:
    max_word = ""
    max_count = 0
    for word in word_count:
        if word_count[word] > max_count:
            max_word = word
            max_count = word_count[word]
    sorted_words.append((max_word, max_count))
    del word_count[max_word]

# print top 10 words
for word, count in sorted_words[:10]:
    print(f"{word} -> {count}")


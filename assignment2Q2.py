#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# open the file
file = open('sample-file.txt', 'r')
content = file.read()
newcontent = ""

# remove commas, keep spaces
for i in content:
    if i != ",":
        newcontent += i

# define letters for manual lowercase conversion
capital_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase_Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# convert to lowercase
lowercasecontent = ""
for i in newcontent:
    if i in capital_letters:
        index = capital_letters.index(i)
        lowercasecontent += lowercase_Letters[index]
    else:
        lowercasecontent += i

# remove punctuation except spaces
no_punctuation_content = ""
for i in lowercasecontent:
    if i in lowercase_Letters or i == " ":
        no_punctuation_content += i

# split into words
words = no_punctuation_content.split()

# keep only words with at least 2 letters
clean_words = []
for word in words:
    if sum(1 for c in word if c in lowercase_Letters) >= 2:
        clean_words.append(word)

# create bigrams
bigrams = []
for i in range(len(clean_words) - 1):
    bigrams.append((clean_words[i], clean_words[i + 1]))

# count bigram frequencies
bigram_count = {}
for bigram in bigrams:
    if bigram in bigram_count:
        bigram_count[bigram] += 1
    else:
        bigram_count[bigram] = 1

# manually sort bigrams by frequency
sorted_bigrams = []
while bigram_count:
    max_bigram = ""
    max_count = 0
    for bigram in bigram_count:
        if bigram_count[bigram] > max_count:
            max_bigram = bigram
            max_count = bigram_count[bigram]
    sorted_bigrams.append((max_bigram, max_count))
    del bigram_count[max_bigram]

# print top 5 bigrams (assignment asks for 5)
for bigram, count in sorted_bigrams[:5]:
    print(bigram[0], bigram[1], "->", count)

file.close()


"""
CP1404 - Practical
Word Occurrences
Estimate: 15 minutes
Actual:
"""

text = input("Text: ")
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.keys())
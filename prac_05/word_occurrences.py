"""
CP1404 - Practical
Word Occurrences
Estimate: 15 minutes
Actual: 20 minutes
"""

text = input("Text: ")
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.keys())

max_length = max(len(word) for word in sorted_words)

for word in sorted_words:
    print(f"{word:{max_length}} : {word_count[word]}")
"""
estimate: 30
actual:
"""

text=input("Text: ")
words=text.split()

word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0)+1


for word in sorted(word_to_count.keys()):
    print(f"{word}: {word_to_count[word]}")
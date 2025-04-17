sentence = "Hello this is a sentence"

word = 0
character = 0
for i in sentence:
    character += 1

print(sentence.split())
print(f"There are total {len(sentence.split())} words in sentence") # words
print(f"There are total {character} characters in sentence (including spaces)")
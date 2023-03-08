# TODO
from cs50 import get_string

s = get_string("Text: ")
# Count the number of words, sentences and letters
# initialize words as 1 as spaces + 1 = number of words
letters = 0
words = 1
sentences = 0
for ch in s:
    if ch == ' ':
        # if its a space, it indicates a word, update words by one
        words += 1
    elif ch in ['.', '?', '!']:
        # if it is a sentence, update sentence by one
        sentences += 1
    elif ch.isalpha():
        # if its a letter, update letters by one
        letters += 1
# Average number of letters per 100 words
L = (letters / words)*100
# Average number of sentences per 100 words
S = (sentences / words)*100
# Formula for calculating grade level
index = 0.0588 * L - 0.296 * S - 15.8
# Print grade level based on index
if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print(f"Grade {round(index)}")
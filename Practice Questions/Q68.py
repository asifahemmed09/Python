"""
Vowel-Starting Words

Take a sentence as input. Split it into words and print how many words start
with a vowel.
"""

sentence = input("Enter a sentence: ")

words = sentence.split()



count = 0
for word in words:
    if word[0] in "aeiouAEIOU":
        count += 1

print(f"{count} words start with a vowel")

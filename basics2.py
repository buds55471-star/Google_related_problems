# 2. Take a string input and count the number of vowels and consonants.
# (Microsoft)

s = input("Enter a string: ").lower()  # convert to lowercase for consistency

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for ch in s:
    if ch.isalpha():  # count only letters
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)

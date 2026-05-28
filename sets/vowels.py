def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    vowels_count = 0
    unique_vowels = set()
    for vowel in text:
        if vowel in vowels:
            vowels_count = vowels_count + 1
            unique_vowels.add(vowel)
    return vowels_count, unique_vowels

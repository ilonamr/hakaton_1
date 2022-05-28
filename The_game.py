import random

# name generator
consonants = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z")
vowels = ("a", "e", "i", "o", "u", "y")


def name_generator(letter_count):
    name = ""
    while letter_count > 0:
        consonant = consonants[random.randint(0, len(consonants) - 1)]
        name += consonant
        letter_count -= 1
        if letter_count == 0:
            break
        vowel = vowels[random.randint(0, len(vowels) - 1)]
        name += vowel
        letter_count -= 1
    return name


print(name_generator(5))

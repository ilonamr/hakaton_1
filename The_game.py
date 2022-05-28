import random

# name generator
consonants = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z")
vowels = ("a", "e", "i", "o", "u", "y")
roman_numbers = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X'
}

aliases = ("Sir", "Don", "Mister")


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
    name = name.capitalize()
    return name


def roman_number_generator():
    roman_number = roman_numbers[random.randint(1, 10)]
    return roman_number


def alias_generator():
    alias = aliases[random.randint(0, 2)]
    return alias


def full_name_generator(letter_count):
    return alias_generator() + " " + name_generator(letter_count) + " " + roman_number_generator()


while (True):
    print("How long name do you want (from 1 to 9 letters)?")
    count = input()
    if(count in "123456789" and len(count) == 1):
        letter_count = int(count)
        print(full_name_generator(letter_count))
    else:
        print("Wrong number or letter please try again")

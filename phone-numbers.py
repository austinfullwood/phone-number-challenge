#!/usr/bin/python3

'''
Given a phone number, the program checks for all
valid combinations of words from a dictionary that
are compatiable with the phone number.

To Run:
./phone-numbers.py <phone-number>
- or -
python3 phone-numbers.py <phone-number>

Example:
./phone-numbers.py 762-5387

Author:     Austin Fullwood
Version:    04.14.21
'''

import sys

# dictionary of valid letters for each number
numbers_to_letters = {
    0: [],
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}

'''
Gets all the possibly valid words from sample_dictionary.txt
for the given phone number.

param:      phone_number    the phone number used to check for
                            valid words in the dictionary
returns:    list of valid characters
'''
def get_all_possible_combinations(phone_number):
    f = open("sample_dictionary.txt", "r")
    output = []
    for x in f:
        x = x[:-1]
        if len(x) == len(phone_number):
            output.append(x)
    return output

'''
Gets a list of valid characters.

params:     number  the number fo
returns:    list of valid characters
'''
def get_letters_for_number(number):
    return numbers_to_letters[number]

'''
Main loop of the program
'''
if __name__ == '__main__':
    # check for phone number
    if (len(sys.argv) < 2):
        exit()
    
    # get phone number, remove valid but not numeric characters ('-', '(', ')', ' '),
    # and check to make sure the rest of the input is numeric
    phone_number = sys.argv[-1]
    phone_number = phone_number.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
    if (not phone_number.isnumeric()):
        exit()
    
    # loops through all the possibly valid words and removes any word that is invalid
    possible_combos = get_all_possible_combinations(phone_number)
    index = 0
    for number in phone_number:
        valid_letters = get_letters_for_number(int(number))
        new_possible_combos = []
        for combo in possible_combos:
            for valid_letter in valid_letters:
                if combo[index] == valid_letter:
                    new_possible_combos.append(combo)
                    break
        possible_combos = new_possible_combos
        index += 1
    
    # prints all the found valid words
    for possible_combo in possible_combos:
        print(possible_combo)
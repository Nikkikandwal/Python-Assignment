#-------------------------------------------------------------------------------
# Name:        module13
# Purpose:
#
# Author:      nikita
#
# Created:     10-03-2024
# Copyright:   (c) nikit 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    vowel_free_string = ''.join(char for char in string if char not in vowels)
    return vowel_free_string


input_string = 'Nikita'
vowel_free = remove_vowels(input_string)
print("String without vowels:", vowel_free)
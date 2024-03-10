#-------------------------------------------------------------------------------
# Name:        module10
# Purpose:
#
# Author:      nikita
#
# Created:     10-03-2024
# Copyright:   (c) nikit 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def long_words(n, str):
    word_len = []
    txt = str.split(" ")


    for x in txt:

        if len(x) > n:
            word_len.append(x)


    return word_len

print(long_words(6, "My name is Nikita Kandwal"))
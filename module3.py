#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      nikita
#
# Created:     10-03-2024
# Copyright:   (c) nikit 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

string= input("Enter string:")

vowels=0

for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):


            vowels=vowels+1

print("Number of vowels are:")
print(vowels)
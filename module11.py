#-------------------------------------------------------------------------------
# Name:        module12
# Purpose:
#
# Author:      nikita
#
# Created:     10-03-2024
# Copyright:   (c) nikit 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

myStr =  input('Enter the binary string : ')


flag = True
for char in myStr :
    if(char == '0' or char == '1'):
       continue
    else :
        flag = False
        print("The String is not a binary string")
        break

if(flag):
    print("The String is binary string")
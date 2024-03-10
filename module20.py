#-------------------------------------------------------------------------------
# Name:        module20
# Purpose:
#
# Author:      nikita
#
# Created:     10-03-2024
# Copyright:   (c) nikit 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def ispalindrome(s):
    return s==s[::-1]
s="madam"
ans= ispalindrome(s)

if ans:
    print("Yes")
else:
    print("No")
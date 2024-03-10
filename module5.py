#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      nikita
#
# Created:     10-03-2024
# Copyright:   (c) nikit 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

num = int(input('Enter the desired number:'))

flag = False

if num > 1:

              for i in range (2, num):

                             if (num % i) == 0:

                                            flag = True

                                            break

if flag:

              print('The number entered is not a prime number')

else:

              print('The number entered is a prime number')
#-------------------------------------------------------------------------------
# Name:        module6
# Purpose:
#
# Author:      nikita
#
# Created:     10-03-2024
# Copyright:   (c) nikit 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

test_list = [(6, 24, 12), (7, 9, 6), (12, 18, 21)]


print("The original list is : " + str(test_list))


K = 6

res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]



print("K Multiple elements tuples")
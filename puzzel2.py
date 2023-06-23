
# Write a Python program that accept a list of integers and check the length and the fifth element.
#  Return true if the length of the list is 8 and fifth element occurs thrice in the said list.

list = [11, 12, 14, 13, 14, 13, 15, 14]
if len(list) == 8 and list.count(list[4]) == 3:
    print("true")
else:
    print("false")

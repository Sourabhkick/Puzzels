# Write a Python program find a list of integers with exactly two occurrences of nineteen and
#   at least three occurrences of five.

list = [19, 19, 15, 5, 3, 5, 5, 2]
if list.count(19)==2 and list.count(5) >=3:
    print("true")
else:
    print("false")
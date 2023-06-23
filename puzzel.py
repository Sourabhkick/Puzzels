
# Find a list of one hundred integers between 0 and 999  which all differ by ten from one another


def test(list):
    return all(i in range(1000) and abs(i - j) >= 10 for i in list for j in list if i != j) and len(set(list)) == 100
nums = list(range(0, 1000, 10))
print("Original list:")
print(nums)
print(" one hundred integers between 0 and 999 which all differ by ten from one another:")
print(test(nums))
nums = list(range(0, 1000, 20))
print("one hundred integers between 0 and 999 which all differ by ten from one another:")
print(test(nums))


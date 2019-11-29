numbers = [3, 4, 5, 23, 5, 7, 8]

# print all numbers form the array
for number in numbers:
    print(number)

# find the maximum number in the array by linear search. This results in O(n) in worst case, space complexity is O(1)
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

print(f"the maximum number from the array = {maximum}")

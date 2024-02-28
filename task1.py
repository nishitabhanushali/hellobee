#Write a Python program to print all positive numbers in a range.
#Your Input and output must look something like this
#Input: list1 = [12, -7, 5, 64, -14] Output: 12, 5, 64 Input: list2 = [12, 14, -95, 3] Output: [12, 14, 3]


def print_positive_numbers(list):
    result = [num for num in list if num > 0]
    print("Output:", result)


list1 = [12, -7, 5, 64, -14]
print_positive_numbers(list1)

list2 = [12, 14, -95, 3]
print_positive_numbers(list2)

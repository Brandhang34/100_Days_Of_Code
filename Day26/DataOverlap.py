with open("file1.txt") as file1:
    list1 = file1.read().splitlines()

with open("file2.txt") as file2:
    list2 = file2.read().splitlines()

result = [int(num) for num in list2 if num in list1]

# Write your code above 👆

print(result)

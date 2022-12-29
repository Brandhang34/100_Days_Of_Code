#FileNotFound

# try:
#     file=open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_messsage:
#     print(f"The key {error_messsage} was not found")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError

height = float(input("height: "))
weight = float(input("weight: "))

if height  > 3:
    raise ValueError ("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
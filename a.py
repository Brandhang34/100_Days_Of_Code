print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_of_people = input("How many people to split the bill? ")

percentage = (int(percentage) / 100) + 1

result = (float(total_bill) / int(num_of_people)) * percentage

print("Each person should pay: " + str(round(result, 2)))
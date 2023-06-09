array = input("Enter an array. Ex: 1 2 3 4 5.")
numbers = array.split()
count = 0
for number in numbers:
    if int(number)%2 == 0:
        count += 1
print("The total of even numbers is/are:" + str(count))
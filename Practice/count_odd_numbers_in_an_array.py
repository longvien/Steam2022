array = input("Enter an array. Ex: 1 2 3 4 5 6.")
numbers = array.split()
count = 0
for number in numbers:
    if int(number)%2 == 1:
        count += 1
print("The total of odd numbers are:" + str(count))
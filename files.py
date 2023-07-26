# 1
name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

# 2
file = open("name.txt", "r")
name = file.read()
file.close()
print(f"Your name is {name}")

# 3
numbers = [17, 42, 400]
file = open("numbers.txt", "w")
for number in numbers:
    file.write(str(number) + "\n")
file.close()

# 4
file = open("numbers.txt", "r")
total = 0
for line in file:
    number = int(line)
    total += number
file.close()
print("The sum of the first two numbers is:", total)


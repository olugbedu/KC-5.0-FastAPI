even_count = 0
odd_count = 0
negative_count = 0
zero_count = 0

print("Welcome to the Number Analyzer!")
print("You can enter up to 5 numbers.\n")

for i in range(5):
    try:
        num = int(input(f"Enter number {i + 1}: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.\n")
        continue

    if num % 2 == 0:
        print("This number is Even.")
        even_count += 1
    else:
        print("This number is Odd.")
        odd_count += 1

    if num > 0:
        print("It's Positive.\n")
    elif num < 0:
        print("It's Negative.\n")
        negative_count += 1
    else:
        print("It's Zero.\n")
        zero_count += 1

print(" Summary ")
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Negative numbers:", negative_count)
print("Zeroes:", zero_count)

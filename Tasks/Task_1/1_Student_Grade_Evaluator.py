passed = 0
failed = 0
excellent = 0

students = int(input("How many students? "))

for _ in range(students):
    name = input("Student name: ")
    s1 = float(input("Score 1: "))
    s2 = float(input("Score 2: "))
    s3 = float(input("Score 3: "))

    average = (s1 + s2 + s3) / 3

    if average < 50:
        print(f"{name}: Fail")
        failed += 1
    elif average < 80:
        print(f"{name}: Pass")
        passed += 1
    else:
        print(f"{name}: Excellent!")
        excellent += 1

print("Summary:")
print("Passed:", passed)
print("Failed:", failed)
print("Excellent:", excellent)

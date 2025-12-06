# to find the factorial of a given positive number using loop

num = int(input("Enter a positive number: "))

fact = 1
for x in range(1, num + 1):
    fact *= x

print("Factorial of", num, "is", fact)

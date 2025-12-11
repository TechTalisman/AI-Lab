# to print the reverse of a number using loop

num = int(input("Enter a number: "))
rev = 0

while num > 0:
    d = num % 10
    rev = rev * 10 + d
    num //= 10

print("Reversed number =", rev)

# to display the sum and average of 5 numbers

numbers = [float(input(f"Enter number {i+1}: ")) for i in range(5)]

total = sum(numbers)
average = total / 5

print("Sum =", total)
print("Average =", average)

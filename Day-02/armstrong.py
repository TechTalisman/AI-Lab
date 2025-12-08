#to check whether a number is Armstrong number or not using loop

num = int(input("Enter a number: "))
n = num
count = 0
while n>0:
    d = n%10
    count+=1
    n = n//10
n = num
sum = 0
while n>0:
    d = n%10
    sum += d**count
    n //= 10
if sum==num:
    print(num,"is an Armstrong Number.")
else:
    print(num,"is not an Armstrong Number.")

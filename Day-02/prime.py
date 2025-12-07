#to check whether a number is Prime number or not using loop

num = int(input("Enter a number: "))
count = 0
for x in range(1,num+1):
    if num%x==0:
        count+=1
if count==2:
    print(num,"is a prime number\n")
else:
    print(num,"is not a prime number\n")

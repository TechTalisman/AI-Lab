#to check and print all Armstrong numbers with in 1000 using loop

print("Armstrong numbers within 1000: ")
for x in range(1,1000):
    n = x
    count = 0
    while n>0:
        d = n%10
        count+=1
        n = n//10
    n = x
    sum = 0
    while n>0:
        d = n%10
        sum += d**count
        n //= 10
    if sum==x:
        print(sum)

n = int(input("Enter the value of n: "))
print("Fibonacci Terms: ")
if n==1:
    print(0)
elif n==2:
    print(0,"",1)
else:
    a = 0
    b = 1
    print(a,end=" ")
    print(b,end=" ")
    for x in range(3,n+1):
        temp = a+b
        a = b
        b = temp
        print(b,end=" ")
  

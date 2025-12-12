# to find out HCF and LCM of two numbers

def hcf_lcm(a, b):
    x, y = a, b
    while y != 0:
        x, y = y, x % y  
    hcf = x
    lcm = (a * b) // hcf
    return hcf, lcm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

hcf, lcm = hcf_lcm(a, b)
print("HCF =", hcf)
print("LCM =", lcm)

# to convert numbers between different number systems

def number_system_conversion():
    print("\nChoose Conversion")
    print("1. Decimal → Binary")
    print("2. Decimal → Hexadecimal")
    print("3. Hexadecimal → Octal")
    print("4. Binary → Decimal")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        n = int(input("Enter decimal number: "))
        print("Binary =", bin(n)[2:])

    elif choice == 2:
        n = int(input("Enter decimal number: "))
        print("Hexadecimal =", hex(n)[2:].upper())

    elif choice == 3:
        hexa = input("Enter hexadecimal number: ")
        decimal = int(hexa, 16)
        print("Octal =", oct(decimal)[2:])

    elif choice == 4:
        b = input("Enter binary number: ")
        decimal = int(b, 2)
        print("Decimal =", decimal)

    else:
        print("Invalid choice")

number_system_conversion()

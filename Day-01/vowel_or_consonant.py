# to display whether an alphabet is a vowel or a consonant

ch = input("Enter an alphabet: ").lower()

if ch.isalpha() and len(ch) == 1:
    if ch in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")

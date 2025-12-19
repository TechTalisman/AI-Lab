# Vacuum Cleaner Problem using a Simple Reflex Agent
# Two-room environment: Room A and Room B
# 0 -> Clean, 1 -> Dirty

# Input validation for Room A status
while True:
    a = int(input("Enter status of Room A (0-Clean, 1-Dirty): "))
    if a in [0, 1]:
        break
    print("Invalid input! Enter only 0 or 1.")

# Input validation for Room B status
while True:
    b = int(input("Enter status of Room B (0-Clean, 1-Dirty): "))
    if b in [0, 1]:
        break
    print("Invalid input! Enter only 0 or 1.")

# Environment representation using dictionary
environment = {'A': a, 'B': b}

# Input validation for starting location
while True:
    location = input("Enter starting location (A/B): ").upper()
    if location in ['A', 'B']:
        break
    print("Invalid location! Enter A or B.")

# Display initial status
print("\nInitial Environment Status:")
print(environment)
print("Vacuum Cleaner is at location:", location)
print("-" * 40)

# Loop continues until both rooms are clean
while environment['A'] == 1 or environment['B'] == 1:

    # If current room is dirty, clean it
    if environment[location] == 1:
        print(f"Room {location} is Dirty. Performing SUCK operation.")
        environment[location] = 0
        print(f"Room {location} is now Clean.")
    else:
        print(f"Room {location} is already Clean.")

    # Move to the other room
    if location == 'A':
        print("Moving RIGHT to Room B.")
        location = 'B'
    else:
        print("Moving LEFT to Room A.")
        location = 'A'

    # Display current environment status
    print("Current Environment Status:", environment)
    print("-" * 40)

# Goal state reached
print("All rooms are clean. Goal achieved!")

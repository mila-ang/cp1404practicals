"""
CP1404 - Practical
Menus
"""

MENU = """(H)ello
(G)oodbye
(Q)uit"""

# Get user's name
name = input("Enter name: ")

# Display menu
print(MENU)

# Get user choice
choice = input(">>> ").upper()  # Convert the input to uppercase to handle both lower and upper cases

# Process user choice until quit (Q)
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    # Display menu again
    print(MENU)

    # Get the next choice from the user
    choice = input(">>> ").upper()

# Display finished message
print("Finished.")

#Activity Instructions
# Demonstrate your understanding of loops by completing the following individual checkpoint assignment.

# Write a Python Program that does each of the following:

# Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as 
# the number is negative, then display the number. For example:


# Please type a positive number: -3
# Sorry, that is a negative number. Please try again.
# Please type a positive number: -8
# Sorry, that is a negative number. Please try again.
# Please type a positive number: -1
# Sorry, that is a negative number. Please try again.
# Please type a positive number: 12
# The number is: 12

#Coding starts here...

number = 0
while number >= 0:
    number = int(input("Please type a positive number: "))
    if number < 0:
        print("Sorry, that is a negative number. Please try again.")
    elif number >= 0:
            print(f"The number is: {number}")
            break

# Import the Stack class
from stack import Stack

# Introduction to the game
print("\nLet's play Towers of Hanoi!!")

# Create the stacks: Left, Middle, and Right
# These stacks represent the rods in the game
stacks = []
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')
stacks += [left_stack, middle_stack, right_stack]

# Set up the game by asking the user for the number of disks they want to play with
num_disks = int(input('\nHow many disks do you want to play with?\n'))

# Ensure the user inputs a valid number of disks (minimum 3 disks for a proper challenge)
while num_disks < 3:
    num_disks = int(input('\nEnter a number greater than or equal to 3\n'))

# Push all the disks to the left stack (initial configuration), starting with the largest disk
for disk in range(num_disks, 0, -1):
    left_stack.push(disk)

# Calculate and display the optimal number of moves using the formula 2^n - 1, where n is the number of disks
num_optimal_moves = (2 ** num_disks) - 1
print('\nThe fastest you can solve this game is in {0} moves.'.format(num_optimal_moves))

# Function to get user input for choosing which stack to move from/to
def get_input():
    # Create a list of the first letter of each stack name (L, M, R) for easy input
    choices = [stack.get_name()[0] for stack in stacks]

    # Keep asking the user until a valid input is provided
    while True:
        # Display the stack choices (Left, Middle, Right) with their corresponding letters
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print('Enter {0} for {1}'.format(letter, name))

        # Take the user's input
        user_input = input('')

        # Check if the input is valid (i.e., if it matches the first letter of a stack's name)
        if user_input in choices:
            # If valid, return the corresponding stack
            for i in range(len(stacks)):
                if user_input == choices[i]:  # Match the input with the stack letter
                    return stacks[i]
        else:
            # If the input is invalid, display an error message and ask again
            print("Invalid input. Please enter a valid stack letter.")

# Initialize the number of user moves
num_user_moves = 0

# Game loop: Keep playing until all disks are on the right stack (i.e., the size of right_stack equals num_disks)
while right_stack.get_size() != num_disks:

    # Display the current state of the stacks
    print('\n\n\n...Current Stacks...')
    for stack in stacks:
        stack.print_items()

    # Input loop: Ask the user to select a stack to move from and a stack to move to
    while True:

        # Ask for the stack to move a disk from
        print('\nWhich stack do you want to move from?')
        from_stack = get_input()

        # Ask for the stack to move the disk to
        print('\nWhich stack do you want to move to?')
        to_stack = get_input()

        # Check if the move is valid:
        # If the from_stack is empty, the move is invalid
        if from_stack.get_size() == 0:
            print('\n\nInvalid move. Try again.')
        
        # If the to_stack is empty or the top disk of from_stack is smaller than the top disk of to_stack, the move is valid
        elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
            # Move the disk by popping it from from_stack and pushing it to to_stack
            disk = from_stack.pop()
            to_stack.push(disk)
            # Increment the user's move count
            num_user_moves += 1
            # Break out of the input loop and return to the game loop
            break
        
        # If the move is invalid (i.e., trying to place a larger disk on a smaller one), display an error message
        else:
            print('\n\nInvalid move. Try again.')

# When the right_stack contains all the disks, the game is complete
print('\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}'.format(num_user_moves, num_optimal_moves))

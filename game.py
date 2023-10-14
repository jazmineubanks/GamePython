# Jazmin Eubanks
# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}
#a list of valid direction commands to navigate through rooms
directions = ['North', 'South', 'East', 'West']

# function: navigate: determines next room and provides appropriate messaging based on players input direction.
def navigate(current_room, direction):
    # If direction is 'exit', return exit message
    if direction == "Exit":
        return 'exit', 'Thanks for playing.'
    #check if player input starts with go followed by direction
    #if true, move to assinged direction base don user input
    if direction.startswith('go '):
        move = direction.split()[1]
        #check if move is a valid direction to move from current room
        if move in rooms[current_room]:
            return (rooms[current_room][move], "")
        #when move is not valid from current room
        else:
            return (current_room, "Sorry! You cannot go to that direction")
    # when player input does not adhere to go direction format
    else:
        return (current_room, "That is not a valid direction. You need to enter one of: ['go North', 'go South', 'go East', 'go West', 'Exit'].")
#function main
#manages the game loop and player interactions
#uses while loop to offer navigation choices, processes those choices until a termination condition is met
def main():
    current_room = 'Great Hall'
    #loop keeps running until broken
    while True:
        #display players location
        print("The player is in", current_room)
        #take direction input from player
        direction = input('Please enter go North, go South, go East or go West: ')
        #call navigate function, store resulting message and new room
        new_room, message = navigate(current_room, direction)
        #display message to user
        print(message)
        if new_room == 'exit':
        	break
        else:
        	current_room = new_room
#start the game by calling main function
main()
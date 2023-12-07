# Author: Sanket Dobaria, Sameer Bhalala
# Date: 12/2/23


from GameEngine import GameEngine

def main():
    """
    Main function to run the game.

    Creates and initializes a GameEngine object, then runs the game loop until all vegetables are collected.

    Displays game information, updates the game state, and handles game over and high score functionality.
    """
    # Instantiate and store a GameEngine object
    game = GameEngine()

    # Initialize the game
    game.initializeGame()

    # Display the game's introduction
    game.intro()

    # Create a variable to store the number of remaining vegetables in the game
    remaining_veggies = game.remainingVeggies()

    # While there are still vegetables left in the game
    while remaining_veggies > 0:
        # Output the number of remaining vegetables and the player's score
        print(f"{remaining_veggies} veggies remaining. Current score: {game.getScore()}")

        # Print out the field
        game.printField()

        # Move the rabbits
        game.moveRabbits()

        # Move the captain
        game.moveCaptain()

        # Move the snake
        game.moveSnake()

        # Determine the new number of remaining vegetables
        remaining_veggies = game.remainingVeggies()

    # Display the Game Over information
    game.gameOver()

    # Handle the High Score functionality
    game.highScore()

if __name__ == "__main__":
    main()

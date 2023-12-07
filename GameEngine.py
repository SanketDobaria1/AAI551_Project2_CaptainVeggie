# Author: Sanket Dobaria, Sameer Bhalala
# Date: 12/2/23

import os
import random
import pickle
from Captain import Captain
from Rabbit import Rabbit
from Veggie import Veggie


class GameEngine:
    """
    Represents the game engine for Captain Veggie.

    Attributes:
    - __field (list): The game field.
    - __rabbits (list): List of rabbit creatures on the field.
    - __captain (Captain): The captain creature on the field.
    - __possible_veggies (list): List of possible vegetable types in the game.
    - __score (int): Current score in the game.
    """

    # Private constants
    NUMBER_OF_VEGGIES = 30
    NUMBER_OF_RABBITS = 5
    HIGHSCORE_FILE = "highscore.data"

    def __init__(self):
        """
        Initialize the GameEngine.
        """

        # Initialize member variables
        self.__field = []
        self.__rabbits = []
        self.__captain = None
        self.__possible_veggies = []
        self.__score = 0

    def initVeggies(self):
        # Prompt the user for the name of the veggie file
        veggie_file_name = input("Please enter the name of the vegetable point file: ")
        while not os.path.exists(veggie_file_name):
            veggie_file_name = input(f"{veggie_file_name} does not exist! Please enter the name of the vegetable point file: ")
        
        with open(veggie_file_name, 'r') as file:
            lines = file.readlines()
            field_size = tuple(map(int, lines[0].split(',')[1:]))
            self.__field = [[None for _ in range(field_size[1])] for _ in range(field_size[0])]

            for line in lines[1:]:
                veggie_data = line.strip().split(",")
                veggie_name, veggie_symbol, veggie_points = veggie_data
                self.__possible_veggies.append(Veggie(veggie_name, veggie_symbol, int(veggie_points)))

        # Randomly place veggies on the field
        for _ in range(self.NUMBER_OF_VEGGIES):
            veggie_index = random.randint(0, len(self.__possible_veggies) - 1)
            veggie = self.__possible_veggies[veggie_index]

            while True:
                x = random.randint(0, len(self.__field[0]) - 1)
                y = random.randint(0, len(self.__field) - 1)

                if self.__field[y][x] is None:
                    self.__field[y][x] = veggie
                    break

    def initCaptain(self):
        # Randomly place the captain on the field
        while True:
            x = random.randint(0, len(self.__field[0]) - 1)
            y = random.randint(0, len(self.__field) - 1)

            if self.__field[y][x] is None:
                self.__captain = Captain(x, y)
                self.__field[y][x] = self.__captain
                break

    def initRabbits(self):
        # Randomly place rabbits on the field
        for _ in range(self.NUMBER_OF_RABBITS):
            while True:
                x = random.randint(0, len(self.__field[0]) - 1)
                y = random.randint(0, len(self.__field) - 1)

                if self.__field[y][x] is None:
                    rabbit = Rabbit(x, y)
                    self.__field[y][x] = rabbit
                    self.__rabbits.append(rabbit)
                    break

    def initializeGame(self):
        """
        Initialize the game by placing vegetables, captain, and rabbits on the field.
        """
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

    def remainingVeggies(self):
        remaining_veggies_count = 0
        for row in self.__field:
            for item in row:
                if isinstance(item, Veggie):
                    remaining_veggies_count += 1

        return remaining_veggies_count

    def intro(self):
        """
        Display the game introduction.
        """

        print("Welcome to Captain Veggie!")

        print("The rabbits have invaded your garden and you must harvest")
        print("as many vegetables as possible before the rabbits eat them")
        print("all! Each vegetable is worth a different number of points")
        print("so go for the high score!\n")
    
        print("The vegetables are:")
        for veggie in self.__possible_veggies:
            print(veggie)
        print("Captain Veggie is V, and the rabbits are R's.")
        print("\nGood luck!")
    
    def printField(self):
        # Create a border around the field
        border = "#" * (len(self.__field[0]) * 3 + 2)

        # Print the field
        print(border)
        for row in self.__field:
            print("#", end="")
            for item in row:
                if item is None:
                    print("   ", end="")
                else:
                    print(f" {item.getSymbol()} ", end="")
            print("#")

        print(border)
    
    def getScore(self):
        """
        Get the current score in the game.

        Returns:
        - int: The current score.
        """
        return self.__score

    def moveRabbits(self):
        """
        Move the rabbit creatures on the field randomly.
        """
        
        for rabbit in self.__rabbits:
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)

            new_x = rabbit.getX() + dx
            new_y = rabbit.getY() + dy

            if 0 <= new_x < len(self.__field[0]) and 0 <= new_y < len(self.__field):
                new_location = self.__field[new_y][new_x]

                if new_location is None or isinstance(new_location, Veggie):
                    # Move rabbit to new location in field
                    self.__field[new_y][new_x] = rabbit

                    # Set rabbit's previous location to None
                    self.__field[rabbit.getY()][rabbit.getX()] = None
                    
                    # Update rabbit's position
                    rabbit.setX(new_x)
                    rabbit.setY(new_y)

                    # If rabbit landed on a veggie, remove the veggie
                    if isinstance(new_location, Veggie):
                        if new_location in self.__possible_veggies:
                            self.__possible_veggies.remove(new_location)
                        # self.__field[new_y][new_x] = None
                # Do not move if the new position is occupied by another Rabbit or Captain object
                else:
                    continue
            # Do not move if the new position is outside the boundaries of the field
            else:
                continue
    
    def moveCptVertical(self, dy):
        new_y = self.__captain.getY() + dy

        if 0 <= new_y < len(self.__field):
            new_location = self.__field[new_y][self.__captain.getX()]

            if new_location is None:

                # Set captain's previous location to None
                self.__field[self.__captain.getY()][self.__captain.getX()] = None

                # Update captain's position
                self.__captain.setY(new_y)

                # Move captain to new location in field
                self.__field[new_y][self.__captain.getX()] = self.__captain

            elif isinstance(new_location, Veggie):
                # Set captain's previous location to None
                self.__field[self.__captain.getY()][self.__captain.getX()] = None

                # Update captain's position
                self.__captain.setY(new_y)

                # Move captain to new location in field
                self.__field[new_y][self.__captain.getX()] = self.__captain

                # Add veggie to captain's collected veggies list
                self.__captain.addVeggie(new_location)

                # Increase the score
                self.__score += new_location.getPoints()

                print(f"Yummy! A delicious {new_location.getName()}!")
            else:
                print("Don't step on the bunnies!")
    
    def moveCptHorizontal(self, dx):
        new_x = self.__captain.getX() + dx

        if 0 <= new_x < len(self.__field[0]):
            new_location = self.__field[self.__captain.getY()][new_x]

            if new_location is None:
                # Set captain's previous location to None
                self.__field[self.__captain.getY()][self.__captain.getX()] = None

                # Update captain's position
                self.__captain.setX(new_x)

                # Move captain to new location in field
                self.__field[self.__captain.getY()][new_x] = self.__captain

            elif isinstance(new_location, Veggie):
                # Set captain's previous location to None
                self.__field[self.__captain.getY()][self.__captain.getX()] = None

                # Update captain's position
                self.__captain.setX(new_x)

                # Move captain to new location in field
                self.__field[self.__captain.getY()][new_x] = self.__captain

                # Add veggie to captain's collected veggies list
                self.__captain.addVeggie(new_location)

                # Increase the score
                self.__score += new_location.getPoints()

                print(f"Yummy! A delicious {new_location.getName()}!")
            else:
                print("Don't step on the bunnies!")

    def moveCaptain(self):
        """
        Move the captain creature based on user input.
        """
        movement_direction = input("Would you like to move up(W), down(S), left(A), or right(D): ").lower()

        if movement_direction == "w":
            if self.__captain.getY() - 1 >= 0:
                self.moveCptVertical(-1)
            else:
                print("You can't move that way!")

        elif movement_direction == "a":
            if self.__captain.getX() - 1 >= 0:
                self.moveCptHorizontal(-1)
            else:
                print("You can't move that way!")

        elif movement_direction == "s":
            if self.__captain.getY() + 1 < len(self.__field):
                self.moveCptVertical(1)
            else:
                print("You can't move that way!")

        elif movement_direction == "d":
            if self.__captain.getX() + 1 < len(self.__field[0]):
                self.moveCptHorizontal(1)
            else:
                print("You can't move that way!")

        else:
            print(f"{movement_direction} is not a valid option")

    def gameOver(self):
        """
        Display the game over information.
        """
        print("GAME OVER!")

        print("You managed to harvest the following vegetables:")
        for veggie in self.__captain.getCollectedVeggies():
            print(veggie.getName())

        print("Your score was: ", self.__score)

    def highScore(self):
        """
        Handle the high score functionality.
        """
        high_scores = []

        if os.path.exists(self.HIGHSCORE_FILE):
            with open(self.HIGHSCORE_FILE, "rb") as f:
                high_scores = pickle.load(f)

        initials = input("Please enter your three initials to go on the scoreboard: ")
        initials = initials[:3]

        if not high_scores:
            high_scores.append((initials, self.__score))
        else:
            new_score = (initials, self.__score)
            for i, score in enumerate(high_scores):
                if self.__score > score[1]:
                    high_scores.insert(i, new_score)
                    break
            else:
                high_scores.append(new_score)

        print("\nHIGH SCORES")
        print("{:<10} {:<5}".format("Name", "Score"))
        for initials, score in high_scores:
            print("{:<10} {:<5}".format(initials, score))

        with open(self.HIGHSCORE_FILE, "wb") as f:
            pickle.dump(high_scores, f)

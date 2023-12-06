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
        veggie_file_name = input("Enter the name of the veggie file: ")
        while not os.path.exists(veggie_file_name):
            veggie_file_name = input("File not found. Enter a valid veggie file name: ")
        
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

# Author: Sanket Dobaria, Sameer Bhalala
# Date: 12/2/23

from Creature import Creature

class Captain(Creature):
    """
    Represents a captain creature, inheriting from Creature.

    :param x: Initial x-coordinate of the captain.
    :type x: int
    :param y: Initial y-coordinate of the captain.
    :type y: int
    """

    def __init__(self, x, y):
        """
        Initialize a new Captain.

        :param x: Initial x-coordinate of the captain.
        :type x: int
        :param y: Initial y-coordinate of the captain.
        :type y: int
        """
        super().__init__(x, y, "V")
        self.__collectedVeggies = []

    def addVeggie(self, veggie):
        """
        Add a vegetable to the captain's collected veggies.

        :param veggie: Vegetable to be added.
        :type veggie: Veggie
        """
        self.__collectedVeggies.append(veggie)

    def getCollectedVeggies(self):
        """
        Get the list of collected vegetables by the captain.

        :return: List of collected vegetables.
        :rtype: list
        """
        return self.__collectedVeggies

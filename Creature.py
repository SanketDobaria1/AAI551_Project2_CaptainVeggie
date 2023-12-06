# Author: Sanket Dobaria, Sameer Bhalala
# Date: 12/2/23


from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    """
    Represents a creature on the field, inheriting from FieldInhabitant.

    :param x: Initial x-coordinate of the creature.
    :type x: int
    :param y: Initial y-coordinate of the creature.
    :type y: int
    :param symbol: Symbol representing the creature.
    :type symbol: str
    """

    def __init__(self, x, y, symbol):
        """
        Initialize a new Creature.

        :param x: Initial x-coordinate of the creature.
        :type x: int
        :param y: Initial y-coordinate of the creature.
        :type y: int
        :param symbol: Symbol representing the creature.
        :type symbol: str
        """
        super().__init__(symbol)
        self.__x = x
        self.__y = y

    def getX(self):
        """
        Get the x-coordinate of the creature.

        :return: x-coordinate of the creature.
        :rtype: int
        """
        return self.__x

    def setX(self, x):
        """
        Set the x-coordinate of the creature.

        :param x: New x-coordinate of the creature.
        :type x: int
        """
        self.__x = x

    def getY(self):
        """
        Get the y-coordinate of the creature.

        :return: y-coordinate of the creature.
        :rtype: int
        """
        return self.__y

    def setY(self, y):
        """
        Set the y-coordinate of the creature.

        :param y: New y-coordinate of the creature.
        :type y: int
        """
        self.__y = y

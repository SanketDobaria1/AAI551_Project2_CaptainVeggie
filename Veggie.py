# Author: Sanket Dobaria, Sameer Bhalala
# Date: 12/2/23


from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
    """
    Represents a vegetable in the field, inheriting from FieldInhabitant.

    :param name: Name of the vegetable.
    :type name: str
    :param symbol: Symbol representing the vegetable.
    :type symbol: str
    :param points: Points associated with the vegetable.
    :type points: int
    """

    def __init__(self, name, symbol, points):
        """
        Initialize a new Veggie.

        :param name: Name of the vegetable.
        :type name: str
        :param symbol: Symbol representing the vegetable.
        :type symbol: str
        :param points: Points associated with the vegetable.
        :type points: int
        """
        super().__init__(symbol)
        self.__name = name
        self.__points = points

    def getName(self):
        """
        Get the name of the vegetable.

        :return: Name of the vegetable.
        :rtype: str
        """
        return self.__name

    def setName(self, name):
        """
        Set the name of the vegetable.

        :param name: New name of the vegetable.
        :type name: str
        """
        self.__name = name

    def getPoints(self):
        """
        Get the points associated with the vegetable.

        :return: Points associated with the vegetable.
        :rtype: int
        """
        return self.__points

    def setPoints(self, points):
        """
        Set the points associated with the vegetable.

        :param points: New points associated with the vegetable.
        :type points: int
        """
        self.__points = points

    def __str__(self):
        """
        Get a string representation of the vegetable.

        :return: String representation of the vegetable.
        :rtype: str
        """
        return f"{self._symbol}: {self.__name} {self.__points} points"

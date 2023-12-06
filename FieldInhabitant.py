# Author: Sanket Dobaria, Sameer Bhalala
# Date: 12/2/23

class FieldInhabitant:
    """
    Represents an inhabitant in the field.

    :param symbol: Symbol representing the inhabitant.
    :type symbol: str
    """

    def __init__(self, symbol):
        """
        Initialize a new FieldInhabitant.

        :param symbol: Symbol representing the inhabitant.
        :type symbol: str
        """
        self._symbol = symbol

    def getSymbol(self):
        """
        Get the symbol representing the inhabitant.

        :return: Symbol representing the inhabitant.
        :rtype: str
        """
        return self._symbol

    def setSymbol(self, symbol):
        """
        Set the symbol representing the inhabitant.

        :param symbol: New symbol representing the inhabitant.
        :type symbol: str
        """
        self._symbol = symbol

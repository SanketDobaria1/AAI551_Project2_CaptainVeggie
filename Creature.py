# Author: Sanket Dobaria, Sameer Bhalala
# Date: 12/2/23


from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def _init_(self, x, y, symbol):
        super()._init_(symbol)
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def getY(self):
        return self._y

    def setY(self, value):
        self._y = value

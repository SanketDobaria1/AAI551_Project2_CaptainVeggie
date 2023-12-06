# Author: Sanket Dobaria, Sameer Bhalala
# Date: 12/2/23


from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
    def _init_(self, name, symbol, points):
        super()._init_(symbol)
        self._name = name
        self._points = points

    def _str_(self):
        return f"{self._symbol}: {self._name} {self._points} points"

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_points(self):
        return self._points

    def set_points(self, value):
        self._points = value

# Author: Sanket Dobaria, Sameer Bhalala
# Date: 12/2/23


class FieldInhabitant:
    def _init_(self, symbol):
        self._symbol = symbol

    def get_symbol(self):
        return self._symbol

    def set_symbol(self, value):
        self._symbol = value

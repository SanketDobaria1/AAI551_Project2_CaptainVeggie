# Author: Sanket Dobaria, Sameer Bhalala
# Date: 12/2/23


from Creature import Creature

class Rabbit(Creature):
    def _init_(self, x, y):
        super()._init_(x, y, "R")

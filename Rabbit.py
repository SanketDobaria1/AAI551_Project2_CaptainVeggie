# Author: Sanket Dobaria, Sameer Bhalala
# Date: 12/2/23


from Creature import Creature

class Rabbit(Creature):
    """
    Represents a rabbit creature, inheriting from Creature.

    :param x: Initial x-coordinate of the rabbit.
    :type x: int
    :param y: Initial y-coordinate of the rabbit.
    :type y: int
    """

    def __init__(self, x, y):
        """
        Initialize a new Rabbit.

        :param x: Initial x-coordinate of the rabbit.
        :type x: int
        :param y: Initial y-coordinate of the rabbit.
        :type y: int
        """
        super().__init__(x, y, "R")

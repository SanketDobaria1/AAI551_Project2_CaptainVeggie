# Author: Sanket Dobaria, Sameer Bhalala
# Date: 12/6/23

from Creature import Creature

class Snake(Creature):
    """
    Snake class, inheriting from Creature.

    :param x: The initial x-coordinate of the snake.
    :type x: int
    :param y: The initial y-coordinate of the snake.
    :type y: int
    """
    def __init__(self, x, y):
        """
        Initialize the Snake object.

        :param x: The initial x-coordinate of the snake.
        :type x: int
        :param y: The initial y-coordinate of the snake.
        :type y: int
        """
        super().__init__(x, y, "S")

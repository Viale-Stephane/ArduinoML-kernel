__author__ = 'pascalpoizat'

from NamedElement import NamedElement


class Brick(NamedElement):
    """
    Abstraction for bricks.

    """

    def __init__(self, name, pin):
        """
        Constructor.

        :param name: String, name of the brick
        :param pin: Integer, pin where the brick is connected
        :return:
        """
        NamedElement.__init__(self, name)
        self.pin = pin

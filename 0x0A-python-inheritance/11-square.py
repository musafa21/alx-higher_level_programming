#!/usr/bin/python3
"""creates a class named Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class named Square

    Attributes:
    attr1(size): size of square
    attr2(area): finds its area
    """
    def __init__(self, size):
        """Initializes an instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return informal string representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)

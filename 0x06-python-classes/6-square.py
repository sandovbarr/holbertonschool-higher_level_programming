#!/usr/bin/python3
""" Class Square that defines a square by
    Private instance attribute: size
    Private instance attirubute: position
    Getter and Setters
    Instantiation with optional size
    size must be an integer
    Public instance method: def area(self)
    Public instance method: def my_print(self)
"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """give us the private attribute size"""
        return self.__size

    @property
    def position(self):
        """give us the private attribute position"""
        return self.__position

    @size.setter
    def size(self, value):
        """set the private attribute size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """set the private attribute position"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if (type(value[0]) != int or type(value[1]) != int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if (value[0] < 0 or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Returns the result of area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square based on square"""
        if self.size != 0:
            if self.position[1] != 0:
                print('\n' * self.position[1], end='')
            for ch in range(self.size):
                print(' ' * self.position[0], end='')
                print('#' * self.size)
        else:
            print()

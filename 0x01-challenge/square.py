#!/usr/bin/python3
""" square class """


class square():
    """ Defines a square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ initializes values for any instance """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ perimeter of the square"""
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """ prints the info of the square"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())

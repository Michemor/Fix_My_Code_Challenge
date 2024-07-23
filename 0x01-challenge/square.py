#!/usr/bin/python3


class Square():
    """ Defines a square """
    width = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimeter of the square"""
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """ string representation of square"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())

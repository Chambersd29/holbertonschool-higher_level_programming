#!/usr/bin/python3


class Rectangle:
    number_of_instance = 0

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instance += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        rectangle_str = ""
        for rows in range(self.__height):
            for columns in range(self.__width):
                rectangle_str += "#"
            if rows < self.__height - 1:
                rectangle_str += "\n"
        return(rectangle_str)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
    
    @property
    def number_of_instances(self):
        return Rectangle.number_of_instances

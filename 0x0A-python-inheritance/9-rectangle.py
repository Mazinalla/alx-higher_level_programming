#!/usr/bin/python3

'''Defines a class Rectangle that inherits from BaseGeometry'''


BaseGeometry = __import__("7-base_geometry.py").BaseGeometry

'''class Rectangle that inherits from BaseGeometry (7-base_geometry.py)'''


class Rectangle(BaseGeometry):

    '''function that Instantiation with width and height'''

    def __init__(self, width, height):

        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

        '''function return the area'''

        def area(self):

            '''return the area'''

            return self.__width * self.__height

        '''function print string'''

        def __str__(self):

            '''return string'''

            return f"[Rectangle] {self.width}/{self.height}"

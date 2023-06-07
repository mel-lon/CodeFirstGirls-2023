# Task 2
import abc


class Shape(object):
   __metaclass__ = abc.ABCMeta

   @abc.abstractmethod
   def calc_perimeter(self, input):
       """Method documentation"""
       return


class Triangle(Shape):

   def __init__(self, a, b, c):
       self.a = a
       self.b = b
       self.c = c

   def calc_perimeter(self):
       perim = self.a + self.b + self.c
       print("Consider me implemented", perim)
       return perim


# Part A
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = 2 * (self.a + self.b)
        print("Consider me implemented:", perim)
        return perim


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


#Part B

rectangle = Rectangle(4, 6)
rectangle_perimeter = rectangle.calc_perimeter()
print("Rectangle perimeter:", rectangle_perimeter)

square = Square(5)
square_perimeter = square.calc_perimeter()
print("Square perimeter:", square_perimeter)

# Task 3 - in markdown
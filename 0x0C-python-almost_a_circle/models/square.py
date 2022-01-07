#!/usr/bin/python3
""" Module that defines class Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ represents a square object """
    def __init__(self, size, x=0, y=0, id=None):
      """ initialize the Square """
      super().__init__(size, size, x, y, id)
      self.size = size

    @property
    def size(self):
      """ size getter """
      return self.height

    @size.setter
    def size(self, value):
      """ size setter """
      self.width = value
      self.height = value

    def __str__(self):
      """ string representation of Square """
      return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width)

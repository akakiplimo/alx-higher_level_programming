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

    def update(self, *args, **kwargs):
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

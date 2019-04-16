from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Vehicle abstract class
    """
    def __init__(self, color):
        pass

    @property
    def color(self):
        if not hasattr(self, "_color"):
            self._color = "(COLOR NOT DEFINED)"
        return self._color

    @color.setter
    def color(self, new_color):
        if not new_color:
            return
        self._color = new_color


class Car(Vehicle):
    """Car Vehicle for filling the slots in parking lot.
    """

    def __init__(self, regnum, color):
        # Initialise Car information
        self._regnum = regnum
        self._color = color

    @property
    def regnum(self):
        if not hasattr(self, "_regnum"):
            self._regnum = "(REGNUM NOT DEFINED)"
        return self._regnum

    @regnum.setter
    def regnum(self, new_regnum):
        if not new_regnum:
            return
        self._regnum = new_regnum


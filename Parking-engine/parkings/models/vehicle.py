class Car(object):
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

    @property
    def color(self):
        if not hasattr(self, "_color"):
            self._color = "(COLOR NOT DEFINED)"
        return self._color


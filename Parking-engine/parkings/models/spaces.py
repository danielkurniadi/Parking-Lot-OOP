class Slots(object):
    """
    Abstract class for any vehicle 1-dimensional containers 
    """

    def __init__(self, size):
        self._size = size
        self._slots = [None]* self._size

    @property
    def size(self):
        return self._size

    # abstract class method
    def get(self, slot_id):
        """
        Get a car at slot with specified number
        Args:
            slot_id (int)
        Returns:
            slot_id (int)
        """
        return self._slots[slot_id-1]

    # abstract class method
    def add(self, slot_id, vehicle):
        """
        Add a car in slots array
        Args:
            slot_id (int)
            vehicle (Vehicle)
        Returns:
            slot_id (int)
        """
        self._slots[slot_id-1] = vehicle
        return slot_id

class CarSlots(Slots):
    pass


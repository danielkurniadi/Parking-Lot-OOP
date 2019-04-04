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
        """ Get a car at slot with specified number.
        Args:
            slot_id (int)
        Returns: (int)
        """
        return self._slots[slot_id-1]

    # abstract class method
    def add(self, slot_id, vehicle):
        """ Add a car in slots array and return the slot id if successful, 
        else return -1.
        Args:
            slot_id (int)
            vehicle (Vehicle)
        Returns: (int)
        """
        if self.is_slot_empty(slot_id):
            self._slots[slot_id-1] = vehicle
            return slot_id
        return -1

    def is_slot_empty(self, slot_id):
        """ Check if slot is empty
        Args:
            slot_id (int)
        Returns: (bool)
        """
        if self._slots[slot_id-1]:
            return False
        return True


class CarSlots(Slots):
    """
    Slots for containing and handle batches of cars.
    """

    def filter_by(self, regnum=None, color=None):
        """Filtering car in slots by car attributes that are specified. Pass all cars in slots 
        if no attribute is specified.
        Args:
            regnum (str): If specified, cars will be filtered by regnum, else ignored
            color (str): If specified, cars will be filtered by color, else ignored
        Returns: 
            [Car]; list of Car objects
        """
        results = []
        slot_ids = []
        for idx, car in enumerate(self._slots):
            if car:
                # Compact boolean logic.
                if ((not regnum) or (car.regnum==regnum)) and\
                        ((not color) or (car.color==color)):
                    results.append(car)
                    slot_id = idx + 1
                    slot_ids.append(slot_id)

        return slot_ids, results

    

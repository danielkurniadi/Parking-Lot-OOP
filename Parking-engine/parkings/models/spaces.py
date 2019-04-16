from abc import ABC, abstractmethod
from parkings.models.vehicle import Car
from parkings.models.helpers.query_mixins import CarsQueryMixin

class Slots(object):
    """
    Abstract class for any vehicle 1-dimensional containers 
    """

    def __init__(self, size=0):
        self._size = size
        self._slots = [None]* self._size

    @property
    def size(self):
        return self._size

    @abstractmethod
    def start_new(self, size):
        """ Start new parking lot or reset.
        Args:
            size (int): size of parking lot.
        """
        self._size = size
        self._slots = [None]* self._size
        return size

    @abstractmethod
    def get(self, slot_id):
        """ Get an item at slots with specified number.
        Args:
            slot_id (int)
        Returns: (int)
        """
        return self._slots[slot_id-1]

    @abstractmethod
    def get_all(self):
        """ Get all items in the slots
        Returns: [Vehicle] list of vehicle object
        """
        return [item for item in self._slots]

    @abstractmethod
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

    @abstractmethod
    def is_slot_empty(self, slot_id):
        """ Check if slot is empty
        Args:
            slot_id (int)
        Returns: (bool)
        """
        if self._slots[slot_id-1]:
            return False
        return True

    @abstractmethod
    def count_vehicle(self):
        """Counting number of vehicle (not None object) in slots array
        """
        count, size = 0, self.size
        for slot_id in range(1, size+1):
            if self.get(slot_id):
                count +=1
        return count

    @abstractmethod
    def delete(self, slot_id):
        """Delete a vehicle 
        """
        if self.is_slot_empty(slot_id):
            return -1
        
        self._slots[slot_id-1] = None
        return slot_id

    @abstractmethod
    def wipe_all(self):
        """ Delete all vehicles in the slots 
        """
        for i in range(self.size):
            self.delete(i+1)


#####################################################################################


class CarSlots(Slots, CarsQueryMixin):
    """
    Representation of parking lot model. 1-Dimensional parking slots that
    handle batch of cars.
    """

    def park(self, regnum, color):
        """Park the incoming car with logic: car is assigned toempty slot nearest to parking gate (neares to slot number 1)
        Args:
            regnum (str): car registration number
            color (str): car color
        Returns:
            slot_id (int): slot number allocated for the car
        """
        slot_id = self.get_nearest_available_id()

        # Check if there is slot available
        car = Car(regnum, color)
        slot_id = self.add(slot_id, car)
        
        return slot_id

    def status(self):
        """Get status of all cars in car slots (parking lot)
        Returns:
            [(str), (str)]: list of tuple (regnum, color)
        """
        # Safe shorcuts to get all Car object != None.
        # Add +1 to id since output is slot number
        cars = self.get_all()
        return [(i+1, car.regnum, car.color) for i, car in enumerate(cars) if car]

    def get_car_by_regnum(self, regnum):
        """Get the first car that match a given registration number specified in the argument
        Args:
            regnum (str): car registration number
        Returns:
            (int), (Car): if found return tuple of slot id and Car object, else -1 and None
        """
        if not regnum:
            return -1, None

        slot_ids, cars = self.filter_by(regnum=regnum)
        
        # Check if there is a match
        if len(cars)<1:
            return -1, None
        
        # Return first car if there are many matches/results
        slot_id, car = slot_ids[0], cars[0]
        return slot_id, car

    def get_cars_by_color(self, color):
        """Filter cars by a specified color
        Args:
            color(str)
        Returns:
            int
        """
        if not color:
            return [], []
        slot_ids, cars = self.filter_by(color=color)

        return slot_ids, cars

    ################################################
    # Utility
    ################################################

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

    def get_nearest_available_id(self):
        """Get nearest slot number to the parking gate that is available
        """
        # iterate through slots in order
        for i in range(self.size):
            if not self._slots[i]:
                return i+1  # slot id start at 1
        return -1

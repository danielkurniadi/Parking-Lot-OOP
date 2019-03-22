import unittest

from parkings.models.vehicle import Car
from parkings.models.spaces import CarSlots


class CarSlotsTest(unittest.TestCase):

    def setUp(self):
        size = 5
        self.carslots = CarSlots(size)

    def tearDown(self):
        self.carslots = None

    def create_add_car(self, slot_id, regnum, color):
        """ Create a Car object and add into car slots
        """
        car = Car(regnum, color)
        idx = self.carslots.add(slot_id, car)
        return idx

    def create_add_cars(self, cars_data):
        """ Create and add multiple Cars object to slots
        """
        for slot_id, regnum, color in cars_data:
            self.create_add_car(slot_id, regnum, color)

    def test_add_car(self):
        """Test adding a new car to the slots returns
        the correct slot id
        """
        exp_slot_id = 5
        regnum, color = "Regnum-123-123", "Color-1"
        slot_id = self.create_add_car(exp_slot_id, regnum, color)
        self.assertEqual(exp_slot_id, slot_id)

    def test_get_car(self):
        """Test getting an existing car in slots returns
        the correct slot id
        """
        exp_slot_id = 5
        regnum, color = "Regnum-123-123", "Color-1"
        slot_id = self.create_add_car(exp_slot_id, regnum, color)
        self.assertEqual(exp_slot_id, slot_id)

    def test_filter_cars_color(self):
        """Test filter cars by color attribute should return
        list of all cars matching the specified color.
        """
        # Setup test variables
        white_cars = [
            (1, "RW-01", "White"),
            (2, "RW-02", "White"),
            (3, "RW-03", "White"),
        ]
        
        black_cars = [
            (4, "BW-04", "Black"),
            (5, "BW-05", "Black")
        ]

        # Create all test cars
        cars = white_cars + black_cars
        self.create_add_cars(cars)
        
        # Verify filters
        white_results = self.carslots.filter_by(color="White")
        for car in white_results:
            self.assertEqual(car.color, "White")

        black_results = self.carslots.filter_by(color="Black")
        for car in black_results:
            self.assertEqual(car.color, "Black")


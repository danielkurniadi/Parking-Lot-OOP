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
        car = Car(regnum, slot_id)
        idx = self.carslots.add(slot_id, car)
        return idx

    def test_add_car(self):
        """Test adding a new car to the slots
        """
        exp_slot_id = 5
        regnum, color = "Regnum-123-123", "Color-1"
        slot_id = self.create_add_car(exp_slot_id, regnum, color)
        self.assertEqual(exp_slot_id, slot_id)

    def test_get_car(self):
        """Test getting existing car in the slots
        """
        exp_slot_id = 5
        regnum, color = "Regnum-123-123", "Color-1"
        slot_id = self.create_add_car(exp_slot_id, regnum, color)
        self.assertEqual(exp_slot_id, slot_id)


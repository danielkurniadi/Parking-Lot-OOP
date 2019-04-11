import unittest

from parkings.core.commands import Command
from parkings.core.controllers import Controller
from parkings.models.vehicle import Car
from parkings.models.spaces import CarSlots

class ControllerTests(unittest.TestCase):
    """Tests case for controller class
    """

    def setUp(self):
        """Setup is called every test
        """
        self.size = 5
        self.parking_lot = CarSlots(self.size)
        self.controller = Controller(self.parking_lot)

    def prepare_empty_lot(self, n):
        """Helper function for setup purpose. Prepare empty lot
        """
        start_new_cmd = "create_parking_lot"
        return self.controller.execute(start_new_cmd, *(n,))

    def prepare_cars(self, n):
        """Helper function for setup purpose. Park multiple cars
        """
        # Setup args
        park_cmd = "park"
        cars_args = [("Regnum-{}".format(idx), "Color-{}".format(idx)) 
            for idx in range(1, n+1)]

        # Prepare an empty parking lot
        self.prepare_empty_lot(n)

        # Park multiple cars
        for arg in cars_args:
            self.controller.execute(park_cmd, *arg)
        return cars_args

    def tearDown(self):
        # tearDown is called every test methods in this class
        self.parking_lot.wipe_all()

    #############################################################################

    def test_execute_start_new(self):
        """Command object is able to execute start new parking lot.
        """
        # Setup params
        n_slots = 10
        start_new_cmd = "create_parking_lot"
        start_new_args = (n_slots,)

        # Verify command is able to execute start new parking lot
        output = self.controller.execute(start_new_cmd, *start_new_args)
        self.assertEqual(output, n_slots)

    def test_execute_park_car(self):
        """Command object is able to execute park car 
        """
        # Setup params
        n_slots = 2
        park_cmd = "park"
        cars_args = [
            ("REG-NUM-01", "Color-1"),
            ("REG-NUM-02", "Color-2")
        ]
        # Prepare parking lot
        self.prepare_empty_lot(n_slots)

        # Park car 0
        slot_id = self.controller.execute(park_cmd, *cars_args[0])
        self.assertEqual(slot_id, 1)

        # Park car 1
        slot_id = self.controller.execute(park_cmd, *cars_args[1])
        self.assertEqual(slot_id, 2)

    def test_execute_leave_car(self):
        """Command object is able to execute delete/leave car command.
        """
        # Setup params
        n_slots = 3
        leave_cmd = "leave"
        self.prepare_cars(n_slots)

        # Verify command is able execute purge command for all cars
        for i in range(1, n_slots+1):
            slot_id = self.controller.execute(leave_cmd, *(i,))
        
        # Verify parking lot is empty
        car_count = self.parking_lot.count_cars()
        self.assertEqual(car_count, 0)
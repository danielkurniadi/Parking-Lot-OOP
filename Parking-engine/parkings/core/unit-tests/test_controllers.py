import unittest

from parkings.core.commands import Command
from parkings.core.commands import EXC_NOT_FOUND_INT
from parkings.core.controllers import Controller
from parkings.models.vehicle import Car
from parkings.models.spaces import CarSlots

class ControllerExecuteTests(unittest.TestCase):
    """Base Test Case for controller class with abstract method for setup
    sub-testcase class.
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
        """Controller is able to execute start new parking lot.
        """
        # Setup params
        n_slots = 10
        start_new_cmd = "create_parking_lot"
        start_new_args = (n_slots,)

        # Verify command is able to execute start new parking lot
        output = self.controller.execute(start_new_cmd, *start_new_args)
        self.assertEqual(output, n_slots)

    def test_execute_park_car(self):
        """Controller is able to execute park car 
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
        """Controller object is able to execute delete/leave car command.
        """
        # Setup params
        n_slots = 3
        leave_cmd = "leave"
        self.prepare_cars(n_slots)

        # Verify command is able execute purge command for all cars
        for i in range(1, n_slots+1):
            slot_id = self.controller.execute(leave_cmd, *(i,))
        
        # Verify parking lot is empty
        car_count = self.parking_lot.count_vehicle()
        self.assertEqual(car_count, 0)

    def test_execute_status(self):
        """Controller object is able to execute status command.
        """
        # Setup params
        n_slots = 3
        status_cmd = "status"

        # Prepare n number of empty slots
        self.prepare_cars(n_slots)

        # Verify command is able to execute without errors
        self.controller.execute(status_cmd)

    def test_execute_queries(self):
        """Controller object is able to execute queries command.
        """
        # Setup params
        n_slots = 5
        query_regnums_by_color = "registration_numbers_for_cars_with_colour"
        query_slotids_by_color = "slot_number_for_registration_number"
        query_slotid_by_regnum = "slot_numbers_for_cars_with_colour"
        commands = [
            (query_regnums_by_color, "Color-2"),
            (query_slotids_by_color, "Color-1"),
            (query_slotid_by_regnum, "Renum-5")
        ]

        # Verify command is able to execute without errors
        for query, arg  in commands:
            self.controller.execute(query, *(arg,))
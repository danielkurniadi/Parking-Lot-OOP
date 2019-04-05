import unittest

from parkings.models.vehicle import Car
from parkings.models.spaces import CarSlots


class CarSlotsTest(unittest.TestCase):

    def setUp(self):
        """Set CarSlots object for each test
        """
        size = 5
        self.carslots = CarSlots(size)

    def tearDown(self):
        """Clean and delete data from previous test
        """
        self.carslots.wipe_all()

    def create_add_car(self, slot_id, regnum, color):
        """ Create a Car object and add into car slots
        """
        car = Car(regnum, color)
        idx = self.carslots.add(slot_id, car)
        return idx

    def park_cars(self, cars_data):
        """ Park multiple cars into car slots
        """
        return [self.carslots.park(regnum, color) for regnum, color in cars_data]

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
            ("RW-01", "White"),
            ("RW-02", "White"),
            ("RW-03", "White"),
        ]
        
        black_cars = [
            ("BW-04", "Black"),
            ("BW-05", "Black")
        ]

        # Create all test cars
        cars = white_cars + black_cars
        self.park_cars(cars)
        
        # Verify color filters
        _, white_results = self.carslots.get_cars_by_color(color="White")
        for car in white_results:
            self.assertEqual(car.color, "White")

        _, black_results = self.carslots.filter_by(color="Black")
        for car in black_results:
            self.assertEqual(car.color, "Black")

        # Verify filter result when no matching
        _, empty_res = self.carslots.get_cars_by_color(color="UNKNOWN")
        self.assertEqual(len(empty_res), 0)

    def test_filter_car_regnum(self):
        """Test filter cars by registration number attribute should return
        only one cars matching the specified registration number.
        """
        # Setup test variables
        car1_regnum = "REGNUM-01-01"
        car2_regnum = "REGNUM-02-02"

        # Create and add test cars
        self.create_add_car(1, car1_regnum, "ANY-COLOR")
        self.create_add_car(2, car2_regnum, "ANY-COLOR")

        # Verify regnum filters
        idx, car1 = self.carslots.get_car_by_regnum(regnum=car1_regnum)
        self.assertEqual(car1.regnum, car1_regnum)
        idx2, car2 = self.carslots.get_car_by_regnum(regnum=car2_regnum)
        self.assertEqual(car2.regnum, car2_regnum)

        # Verify filter result when no matching
        _, empty_res = self.carslots.get_car_by_regnum(regnum="UNKNOWN")
        self.assertIsNone(empty_res)

    def test_leave_car(self):
        """Test delete car by slot id should remove the car object from the slots 
        and return the slot id of the removed car when successful.
        """
        # Setup test variables
        slot_id = 4
        regnum, color = "REGNUM-01-01", "Color-01"
        slot_id = self.create_add_car(slot_id, regnum, color)

        # Delete car when car is in slot_id
        idx = self.carslots.delete(slot_id)
        self.assertEqual(slot_id, idx)

        # Try delete car when car already leave will give -1 signal
        err_sig = self.carslots.delete(slot_id)
        self.assertEqual(-1, err_sig)

    def test_full_slots(self):
        """Test car slots that is full cannot be added. If addition is force
        when slots is full, then assignment is not successful and return -1 signal
        """
        # Setup test variables
        cars_data = [
            ("RW-01", "White"),
            ("RW-02", "White"),
            ("RW-03", "White"),
            ("BW-04", "Black"),
            ("BW-05", "Black")
        ]
        self.park_cars(cars_data)

        # Verify slots is full
        self.assertEqual(self.carslots.size, self.carslots.count_vehicle())

        # Try add one more cars into full slots
        regnum, color = "Regnum-6", "Yellow"
        sig = self.carslots.park(regnum, color)
        
        # Verify park methods return -1 signal
        self.assertEqual(-1, sig)

        # Verify car is not assigned anywhere/ override anything
        idx, car = self.carslots.get_car_by_regnum(regnum)
        self.assertEqual(-1, idx)
        self.assertFalse(car)

    def test_park_slot_assignment(self):
        """When a car is added to one of the slots using park method,
        the car should be assigned to empty slot nearest to parking gate
        """
        # Setup test variables on initially empty slots
        n_cars = 5
        cars_data = [
            ("RW-01", "White"),
            ("RW-02", "White"),
            ("RW-03", "White"),
            ("BW-04", "Black"),
            ("BW-05", "Black")
        ]
        new_car_data = ("NW-06", "Yellow")

        # Park all cars to fill all slots and get the slot numbers
        # then verify that slot numbers is given in increment order.
        ids = self.park_cars(cars_data)
        self.assertEqual(ids, [i for i in range(1, n_cars+1)])

        # Delete a car in the middle and get the slot number which becomes empty
        del_idx = self.carslots.delete(2)

        # Park a new car in and verify that this car is assigned to the slot
        # nearest to parking gate, which was from deleted car
        park_idx = self.carslots.park(*new_car_data)
        self.assertEqual(del_idx, park_idx)

       def test_no_matches_query(self):
        """Test query mixins helper methods. Verify that when no matches found, 
        query returns appropriate signal indicating no match.

        Signal: -1 (int) or None (object) for single query, 
                [] if for bulk query result.
        """
        # start with empty slots, 
        # then query the slots and expect to get no match
        regnums = self.carslots.query_regnums_by_color("Color-99")
        self.assertEqual(len(regnums), 0)

        ids = self.carslots.query_slotids_by_color("Color-99")
        self.assertEqual(len(ids), 0)

        idx = self.carslots.query_slotid_by_regnum("Regnum-99")
        self.assertEqual(idx, -1)

    def test_queries_by_color(self):
        """Test query by color methods from mixins. Verify that when matches found, 
        query returns correct values.
        """
        # Prepare cars for query test
        white_cars = [
            ("RW-01", "White"),
            ("RW-02", "White"),
            ("RW-03", "White"),
        ]
        
        black_cars = [
            ("BW-04", "Black"),
            ("BW-05", "Black")
        ]

        # Park cars for query test
        for car in (white_cars + black_cars):
            self.carslots.park(*car)
        
        # Querying regnum from cars' color: White
        query_res = self.carslots.query_regnums_by_color("White")
        self.assertEqual(query_res, [car[0] for car in white_cars])
        
        # Querying regnum from cars' color: Black
        query_res = self.carslots.query_regnums_by_color("Black")
        self.assertEqual(query_res, [car[0] for car in black_cars])

    def test_queries_by_regnum(self):
        # Prepare cars for query test
        cars_data = [
            ("RW-91", "White"),
            ("RW-92", "White"),
            ("RW-93", "White"),
            ("BW-04", "Black"),
            ("BW-05", "Black")
        ]

        # Park cars for query test
        for car in cars_data:
            self.carslots.park(*car)
        
        # Querying regnum from car (unique) registration number
        for i, (regnum, _) in enumerate(cars_data):
            slot_id = i+1
            query_res = self.carslots.query_slotid_by_regnum(regnum)
            self.assertEqual(query_res, slot_id)


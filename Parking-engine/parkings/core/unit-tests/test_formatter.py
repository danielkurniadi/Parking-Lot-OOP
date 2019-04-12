import unittest
from parkings.core.controllers import Controller
from parkings.models.spaces import CarSlots

class FormatterTest(unittest.TestCase):
    """Test cases on formatting output.
    """

    def setUp(self):
        self.size = 5
        self.parking_lot = CarSlots(self.size)
        self.controller = Controller(self.parking_lot)

    def test_format_start_new_output(self):
        """Formatter is able to format ouputs for start new parking lot command
        """
        # Setup params and mock result of parking lot execution
        start_new_cmd = "create_parking_lot"
        result = 5

        # Verify formatting is correct
        success, output = self.controller.format_start_new_output(result)
        self.assertTrue(success)
        self.assertEqual(output, "Created a parking lot with {} slots".format(result))

    def test_format_park_output(self):
        """Formatter is able to format outputs for park car command
        """
        # Setup params and mock result for successfully parking a car
        park_cmd = "park"
        success_result, fail_result = 3, -1

        # Mock success resp and verify formatting is correct
        success, output = self.controller.format_park_output(success_result)
        self.assertTrue(success)
        self.assertEqual(output, "Allocated slot number: {}".format(success_result))

        # Mock fail resp and verify formatting is correct
        success, output = self.controller.format_park_output(fail_result)
        self.assertFalse(success)
        self.assertEqual(output, "Sorry, parking lot is full")

    def test_format_leave_output(self):
        """Formatter is able to format outputs for leave parking command
        """
        # Setup params and mock result for car successfully leave parking lot
        leave_cmd = "leave"
        slot_id = 1

        # Mock success resp and verify
        success, output = self.controller.format_leave_output(slot_id)
        self.assertTrue(success)
        self.assertEqual(output, "Slot number {} is free".format(slot_id))






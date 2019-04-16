import os
import unittest

from parkings.core.commands import Command
from parkings.core.controllers import Controller
from parkings.models.spaces import CarSlots
from parkings.models.vehicle import Car

from parkings.client.session import Session, EXIT_SIG1

FILE_PATH = os.path.dirname(os.path.realpath(__file__))

class NonInteractiveSessionTests(unittest.TestCase):

    def setUp(self):
        """Setup is called every test methods in this class
        """
        # Prepare input file
        self._filename = "file_input.txt"
        self.filepath = os.path.join(FILE_PATH, "temp/{}".format(self._filename))
        self.erase_file_content()

        # Setup a non-interactive session.
        self.session = Session(False, self.filepath)

    def prepare_mock_file(self):
        """Prepare a scenario for functional tests
        """
        f = open(self.filepath, "w+")

        # Prepare mock commands
        commands = [
            "create_parking_lot 6\n",
            "park KA-01-HH-1234 White\n",
            "park KA-01-HH-9999 White\n",
            "park KA-01-BB-0001 Black\n",
            "park KA-01-HH-7777 Red\n",
            "park KA-01-HH-2701 Blue\n",
            "park KA-01-HH-3141 Black\n",
            "leave 4\n",
            "status\n",
            "park DL-12-AA-9999 White\n",
            "registration_numbers_for_cars_with_colour White\n",
            "slot_numbers_for_cars_with_colour White\n",
            "slot_number_for_registration_number KA-01-HH-3141\n",
        ]

        for command in commands:
            f.write(command)

        f.close()

    def tearDown(self):
        # tearDown is called every test methods in this class
        self.session.parking_lot.wipe_all()
        self.erase_file_content()

    def erase_file_content(self):
        # Valid hack to erase file content
        open(self.filepath, "w+").close()

    ######################################################################

    def test_parse_method_on_empty(self):
        """Parsing an empty inputs should be handled 
        smoothly without error
        """
        # Setup by opening an input file to mock session reader
        f = open(self.filepath, "r")
        inputs = f.readline()
        # Parse input and verify
        parsed_inputs = self.session.parse_inputs(inputs)
        self.assertEqual(parsed_inputs, EXIT_SIG1)

    def test_get_method_on_empty(self):
        """Parsing and getting empty inputs using `get_command_and_args()` 
        should be run smoothly without error
        """
        # Get command and args
        parsed_inputs = self.session.get_command_and_args()
        self.assertEqual(parsed_inputs, EXIT_SIG1)

    def test_run_empty_input(self):
        """Running session using `run()` method when file inputs is empty (no content)
        should run session smoothly without error.
        """
        # Run session on empty file input
        self.session.run()

    def test_full_run(self):
        """Test non-interactive session works for all valid commands.
        Can be considered a candidate for functional test?
        """
        # Run session on an input file with commands
        self.prepare_mock_file()
        self.session.run()

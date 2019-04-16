import sys
from parkings.core.commands import Command
from parkings.core.controllers import Controller
from parkings.models.spaces import CarSlots as ParkingLot

EXIT_SIG = "Exit"
DEBUG = False
IGN_FAIL = True

class Session():
    def __init__(self, is_inter=False, filepath=""):
        self._is_interactive = True
        self._filepath = filepath
        self._reader = sys.stdin if is_inter else open(filepath, "r")
        self.parking_lot = ParkingLot()
        self.controller = Controller(self.parking_lot)

    @property
    def is_interactive(self):
        return self._is_interactive

    def set_running_mode(self, is_inter=True, filepath=""):
        # Assign reader for appropriate session based 
        # on user interaction type. File path must be specified if is_inter is True
        self._is_interactive = is_inter
        self._reader = sys.stdin if is_inter else open(filepath, "r")

    def run(self):
        if DEBUG:
            if self.is_interactive:
                print("Starting interactive mode...")
                print("Type your commands below:")
            else:
                print("Reading from file input...")
                print("Processing... Here are the results:")

        # Check whether session should keep running or exit
        while True:
            inputs = self.get_raw_inputs()
            # Checking for exit signal from user/file input
            if not inputs or inputs == EXIT_SIG:
                break

            cmd_string, args = self.parse_inputs(inputs)
            if not args:
                success, resp = self.controller.execute(cmd_string)
            else:
                success, resp = self.controller.execute(cmd_string, *args)
            # If fail is not ignored, then will quit immediately after failing.
            if not success:
                if DEBUG:
                    print(resp)
                if not IGN_FAIL:
                    break
                continue

            # Write command to STDOUT
            success, output = self.controller.process_output(cmd_string, resp)
            print(output)

        return

    def get_raw_inputs(self):
        input_line = self._reader.readline()
        if (not input_line) or (input_line == EXIT_SIG):
            return EXIT_SIG

        return input_line.split()

    def parse_inputs(self, inputs):
        # Check if no string in inputs
        if len(inputs) < 1:
            return EXIT_SIG

        cmd_string = inputs[0]
        # Check if only one word in inputs
        if len(inputs)<=1:
            return cmd_string, None

        args = inputs[1:]
        for i in range(len(args)):
            if args[i].isnumeric():
                args[i] = int(args[i])
        return cmd_string, tuple(args)


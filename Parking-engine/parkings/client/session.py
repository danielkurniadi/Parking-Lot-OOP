import sys
from parkings.core.commands import Command
from parkings.core.controllers import Controller
from parkings.models.spaces import CarSlots as ParkingLot

EXIT_SIG = "EXIT"
EXIT_SIG1 = "Exit"
EXIT_SIG2 = "\n"
EXIT_SIG3 = ""

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
        if self.is_interactive:
            print("Starting interactive mode...")
            print("Type your commands below:")
        else:
            print("Reading from file input...")
            print("Processing... Here are the results:")
        # Get and parse inputs from users

        # Check whether session should keep running or exit
        while True:
            rawinput = self.get_raw_inputs()
            if rawinput.strip().lower() in [EXIT_SIG.lower(), EXIT_SIG2, EXIT_SIG3]:
                break 

            cmd_string, args = self.parse_inputs(rawinput.split())
            # print(cmd_string, args)
            if not args:
                # print("STATUS")
                success, resp = self.controller.execute(cmd_string)
            else:
                success, resp = self.controller.execute(cmd_string, *args)

            if not success:
                print(resp)
                break

            # Write command to STDOUT
            success, output = self.controller.process_output(cmd_string, resp)
            print(output)

        if self._is_interactive:
            print("Good bye, :)")

        return

    def get_raw_inputs(self):
        input_line = self._reader.readline()
        return input_line

    def parse_inputs(self, inputs):
        # Check if no string in inputs

        cmd_string = inputs[0]
        # Check if only one word in inputs
        if len(inputs)<=1:
            return cmd_string, None

        args = inputs[1:]
        for i in range(len(args)):
            if args[i].isnumeric():
                args[i] = int(args[i])
        return cmd_string, tuple(args)


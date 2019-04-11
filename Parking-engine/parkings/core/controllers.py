
from parkings.core.commands import Command
from parkings.models.vehicle import Car
from parkings.models.spaces import CarSlots

EXC_SIG_INT = -1
EXC_SIG_STR = ""
EXC_SIG_LIST = []

class BaseController():
    """Abstract class for Parking Lot Controller
    """

    def __init__(self, parking_lot):
        # Map command string to parking lot function
        # Don't forget to update the map here when extending the commands in commands.py
        parking_lot = CarSlots()
        self.CMD_MAP = {
            Command.CREATE: {
                "func": parking_lot.start_new,
                "formater": self.format_start_new_output
                },
            Command.PARK: {
                "func": parking_lot.park,
                "formater": self.format_park_output
                },
            Command.LEAVE: {
                "func": parking_lot.purge,
                "formater": self.format_purge_output
                },
            
        }

    # abstract class method
    def execute(self, cmd_string, *args):
        pass

class Controller(BaseController):
    """Command wrapper for command input. This wrapper unifies all input, 
    be it from interactive session or text file input. Command wrapper
    serve as core controller that interact with the models.
    """

    def execute(self, cmd_string, *args):
        """Execute command by calling the models' methods and handle the 
            result/responses from the models.
        Args:
            cmd_string (str): the string representing a command
            *args (tuple): the arguments to run the command
        Returns: the response from parking lot for a specific command
        """
        try:
            func = self.CMD_MAP[cmd_string]["func"]
            # Execute and pass argument args if args is not none
            resp = None
            resp = func() if not args else func(*args)
            return resp

        except KeyError:
            raise Exception("COMMAND NOT FOUND: {}".format(cmd_string))




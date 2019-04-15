from parkings.core.commands import Command
from parkings.models.vehicle import Car
from parkings.models.spaces import CarSlots

from parkings.core.helpers.supports import FormatSupport

EXIT_SIG = "EXIT"
EXIT_SIG1 = "Exit"
EXIT_SIG2 = "\n"
EXIT_SIG3 = ""

class BaseController():
    def execute(self, cmd_string, *args):
        pass

    def process_output(self, cmd_string, resp):
        pass

#################################################################################

class Controller(BaseController, FormatSupport):
    """Command wrapper for command input. This wrapper unifies all input, 
    be it from interactive session or text file input. Command wrapper
    serve as core controller that interact with the models.
    """

    def __init__(self, parking_lot):
        parking_lot = CarSlots()
        self.CMD_MAP = {
            Command.CREATE: {
                "func": parking_lot.start_new,
                "formatter": self.format_start_new_output
                },
            Command.PARK: {
                "func": parking_lot.park,
                "formatter": self.format_park_output
                },
            Command.LEAVE: {
                "func": parking_lot.delete,
                "formatter": self.format_leave_output
                },
            Command.STATUS: {
                "func": parking_lot.status,
                "formatter": self.format_status_output
                },
            Command.QUERY_REGNUMS_BY_COLOR: {
                "func": parking_lot.query_regnums_by_color,
                "formatter": self.format_query_many_output
                },
            Command.QUERY_SLOTNUM_BY_REGNUM: {
                "func": parking_lot.query_slotid_by_regnum,
                "formatter": self.format_query_single_output
                },
            Command.QUERY_SLOTNUMS_BY_COLOR: {
                "func": parking_lot.query_slotids_by_color,
                "formatter": self.format_query_many_output
                }
        }

    def execute(self, cmd_string, *args):
        """Execute command by calling the models' methods and handle the 
            result/responses from the models.
        Args:
            cmd_string (str): the string representing a command
            *args (tuple): the arguments to run the command

        Returns: the response from parking lot for a specific command
        """
        success = True
        try:
            func = self.CMD_MAP[cmd_string]["func"]
            # Execute and pass argument args if args is not none
            resp = None
            resp = func() if not args else func(*args)
            return success, resp

        except KeyError:
            success = False
            return success, "COMMAND NOT FOUND: {}".format(cmd_string)

    def process_output(self, cmd_string, resp):
        """Process the response to formated output given the command 
        type related to the output.

        Args:
            cmd_string (str): the string representing a command
        """
        try:
            func = self.CMD_MAP[cmd_string]["formatter"]
            # Format output and pass processed output to session
            output = None
            # function receive a response which can be single or multiple items
            output = func(resp)
            return output
        
        except KeyError:
            success = False
            return success, "Format function not implemented/ not available for the specified command"
             
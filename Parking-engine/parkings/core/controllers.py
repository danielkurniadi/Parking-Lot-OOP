from parkings.core.commands import Command
from parkings.models.vehicle import Car
from parkings.models.spaces import CarSlots

from parkings.core.helpers.supports import FormatSupport



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
                "formater": self.format_start_new_output
                },
            Command.PARK: {
                "func": parking_lot.park,
                "formater": self.format_park_output
                },
            Command.LEAVE: {
                "func": parking_lot.delete,
                "formater": self.format_leave_output
                },
            Command.STATUS: {
                "func": parking_lot.status,
                "formater": self.format_status_output
                },
            Command.QUERY_REGNUMS_BY_COLOR: {
                "func": parking_lot.query_regnums_by_color,
                "formater": self.format_query_many_output
                },
            Command.QUERY_SLOTNUM_BY_REGNUM: {
                "func": parking_lot.query_slotid_by_regnum,
                "formater": self.format_query_single_output
                },
            Command.QUERY_SLOTNUMS_BY_COLOR: {
                "func": parking_lot.query_slotids_by_color,
                "formater": self.format_query_many_output
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
        try:
            func = self.CMD_MAP[cmd_string]["func"]
            # Execute and pass argument args if args is not none
            resp = None
            resp = func() if not args else func(*args)
            return resp

        except KeyError:
            raise Exception("COMMAND NOT FOUND: {}".format(cmd_string))



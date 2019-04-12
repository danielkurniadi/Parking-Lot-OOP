
from parkings.core.commands import Command
from parkings.models.vehicle import Car
from parkings.models.spaces import CarSlots

EXC_SIG_INT = -1
EXC_SIG_STR = ""
EXC_SIG_LIST = []

class CommandSupport():
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

class BaseController():

    def execute(self, cmd_string, *args):
        pass

    def process_output(self, cmd_string, resp):
        pass

#################################################################################

class Controller(BaseController, CommandSupport):
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

    def format_start_new_output(self, resp):
        OUT_SKELETON = "Created a parking lot with {} slots"
        FAIL_CREATE_ERROR_MSG = "Failed to create a parking lot"

        if resp == EXC_SIG_INT:
            success = False
            return success, FAIL_CREATE_ERROR_MSG

        success = True
        return success, OUT_SKELETON.format(resp)

    def format_park_output(self, resp):
        OUT_SKELETON = "Allocated slot number: {}"
        FULL_EXC_MSG = "Sorry, parking lot is full"

        if resp == EXC_SIG_INT:
            success = False
            return success, FULL_EXC_MSG

        success = True
        return success, OUT_SKELETON.format(resp)

    def format_leave_output(self, resp):
        OUT_SKELETON = "Slot number {} is free"
        ERROR_MSG = "Failed to delete car from slot number {}"

        if resp == EXC_SIG_INT:
            success = False
            return success, ERROR_MSG.format(resp)

        success = True
        return success, OUT_SKELETON.format(resp)

    def format_status_output(self, resp):
        OUT_SKELETON = "{:<12}{:19}{}"
        OUT_HEADER = OUT_SKELETON.format("Slot No.", "Registration No", "Colour")
        output = [OUT_HEADER]

        for slot_id, regnum, color in resp:
            output.append(OUT_SKELETON.format(slot_id, regnum, color))

        success = True
        return success, "\n".join(output)

    def format_query_single_output(self, resp):
        NOT_FOUND_MSG = "Not found"
        if resp and resp != EXC_SIG_INT:
            success = True
            return success, resp

        return False, NOT_FOUND_MSG

    def format_query_many_output(self, resp):
        NOT_FOUND_MSG = "Not found"
        if resp:
            resp = [str(item) for item in resp]
            success = True
            return success, ", ".join(resp)

        return False, NOT_FOUND_MSG


EXC_NOT_FOUND_INT = -1

class Command():
    """Command wrapper for command input. This wrapper unifies all input, 
    be it from interactive session or text file input. Command wrapper
    serve as core controller that interact with the models.
    """
 
    # enumerate available command types. 
    # add and command list here for extention.
    CREATE = "create_parking_lot"
    PARK = "park"
    LEAVE = "leave"
    STATUS = "status"
    QUERY_REGNUMS_BY_COLOR = "registration_numbers_for_cars_with_colour"
    QUERY_SLOTNUM_BY_REGNUM = "slot_number_for_registration_number"
    QUERY_SLOTNUMS_BY_COLOR = "slot_numbers_for_cars_with_colour"

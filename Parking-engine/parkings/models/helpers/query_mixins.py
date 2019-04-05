class CarsQueryMixin(object):
    """Mixins class which is an extention of CarSlots class. 
    Here are query methods that wraps the filtering methods for convenience.
    """
    # abstract class, don't use outside subclass
    def query_regnums_by_color(self, color):
        """Query registration number of cars in parking lots that has
        the specified color.
        Args:
            color (str): specified color for cars query
        Returns:
            (list of str): if found any return list of registration number, else empty list
        """
        if not color:
            return []

        _, cars = self.get_cars_by_color(color)
        if not cars:
            return []

        results = [car.regnum for car in cars]
        return results

    # abstract class, not to be used outside subclass
    def query_slotids_by_color(self, color):
        """Query registration number of cars in parking lots that has the specified color.
        Args:
            color (str): specified color for cars query
        Returns:
            (list of int): if found any return list of slot number, else empty list
        """
        if not color:
            return []

        slot_ids, _ = self.get_cars_by_color(color)
        return slot_ids

    # abstract class, not to be used outside subclass
    def query_slotid_by_regnum(self, regnum):
        """Query registration number of cars in parking lots that has the specified color.
        Args:
            regnum (str): specified color for cars query
        Returns:
            (int): if found, return slot number, else return -1
        """
        if not regnum:
            return -1
        
        slot_id, _ = self.get_car_by_regnum(regnum)
        return slot_id
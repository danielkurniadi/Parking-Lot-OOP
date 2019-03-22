import unittest

from parkings.models.vehicle import Car 

class CarTestsCase(unittest.TestCase):

    def prepare_car(self):
        """Create a car object
        """
        regnum, color = "Regnum-0123-0123", "Color-0"
        return Car(regnum, color)

    def test_car_getter(self):
        """Test car regnum and color getter method returns exactly as owned value
        """
        regnum, color = "Regnum-0123-0912", "color-1"
        car = Car(regnum, color)
        # Get car registration number using getter and verify
        self.assertEqual(car.regnum, regnum)
        # Get car color using getter and verify
        self.assertEqual(car.color, color)

    def test_car_set_regnum(self):
        """Test car regnum setter are working and regnum property can be modified.
        """
        # Setup
        newregnum = "NewRegnum-0123-0123"
        car = self.prepare_car()
        # Set car regnum using setter method and verify 
        car.regnum = newregnum
        self.assertEqual(car.regnum, newregnum)

    def test_car_color(self):
        """Test car color setter are working and color property can be modified.
        """
        # Setup
        newcolor = "newColor-123"
        car = self.prepare_car()
        # Set car regnum using setter method and verify 
        car.color = newcolor
        self.assertEqual(car.color, newcolor)


    
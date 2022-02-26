from random import randint
from datetime import date, time

"""Classes for melon orders."""
class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    
    order_type = None
    tax = 0
 
    def __init__(self, species, qty):
       """Initialize melon order attributes."""
       
       self.species = species
       self.qty = qty
       if qty > 100:
           raise TooManyMelonsError()
       self.shipped = False    
    
    @staticmethod
    def get_base_price():
        """set a random base price between 5 and 9"""
        base_price = randint(5,9)
        if date.weekday(date.today()) in range(0,5):
                if time.hour() in range(8,12):
                    base_price += 4
        return base_price
        
    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        total = (1 + self.tax) * self.qty * base_price
        if self.species == "Christmas melon":
            total *= 1.5
        elif self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08
    
    # def __init__(self, species, qty):
        
    #     self.species = species
    #     self.qty = qty
    #     self.shipped = False


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """ For government orders"""
    order_type = "domestic"

    def __init__(self, species, qty, passed_inspection):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.passed_inspection = False
    
    def mark_inspection(self, passed):
        """Marks inspections as 'passed' """
        if passed:
            self.passed_inspection = True

class TooManyMelonsError(Exception):
    """Raised when someone tries to order more than 100 melons"""
    def __init__(self):
        #self.message = message
        super().__init__("Too many melons!")
        #self.message="Too many melons!"
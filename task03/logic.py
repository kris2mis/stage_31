from laptop import Laptop
from creator import LaptopCreator


class Logic:
    @staticmethod
    def calculate_price(laptops):
        total_price = 0
        for laptop in laptops:
            if isinstance(laptop, Laptop):
                total_price = total_price + laptop._price

        return total_price
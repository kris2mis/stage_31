from laptop import Laptop
from creator import LaptopCreator


class Logic:
    @staticmethod
    def calculate_price(ls):
        total_price = 0
        for price in ls:
            if isinstance(price, Laptop):
                total_price = total_price+ price

        return total_price
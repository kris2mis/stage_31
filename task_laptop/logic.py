from laptop import Laptop
from creator import LaptopCreator


class Logic:
    @staticmethod
    def calculate_price(laptops):
        total_price = 0
        for laptop in laptops:
            if isinstance(laptop, Laptop):
                total_price += laptop._price

        return total_price

    @staticmethod
    def find_expensive_laptop (laptops):

        if not isinstance(laptops, (list, tuple)):
            return

        ilaptop = 0  # индекс

        for index in range(1, len(laptops)):
            if isinstance(laptops[index], Laptop):
                if laptops[index].price > laptops[ilaptop].price:
                    laptops[ilaptop].price = laptops[index].price

            return laptops[ilaptop]

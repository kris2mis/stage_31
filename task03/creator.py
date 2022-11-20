import random
import string
from laptop import Laptop


# генерация людей - это функциональный класс
class LaptopCreator:

    @staticmethod
    def create(size):
        BRAND = ("Apple", "Acer", "Asus", "HP", "Lenovo", "Dell",
                 "Xiomi", "HP", "Huawey")  # tuple

        MAX_PRICE = 2000
        MIN_PRICE = 500

        MODEL = string.ascii_uppercase  # вместо модели исплользовать букву

        ls = []

        for _ in range(size):
            brand = random.choice(BRAND)  # метод choice
            model = MODEL[random.randrange(len(MODEL))]
            price = random.randint(MIN_PRICE, MAX_PRICE)

            laptop = Laptop(brand, model, price)

            ls.append(laptop)

        return ls

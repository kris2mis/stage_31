from laptop import Laptop
from logic import Logic
from creator import LaptopCreator
from convertor import Convertor


def main():
    ls = LaptopCreator.create(5)
    print(Convertor.convert_to_string(ls))

    calc_total_price = Logic.calculate_price(ls)
    expensive_laptop = Logic.find_expensive_laptop(ls)

    print(f"Total count: {calc_total_price}$")
    print(f"\nThe most expensive laptop is {expensive_laptop}")


if __name__ == "__main__":
    main()
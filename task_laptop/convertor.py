from laptop import Laptop

class Convertor:

    @staticmethod
    def convert_to_string(laptops):
        s = "List of laptops:\n"

        if not isinstance(laptops, (list, tuple)):
            return "List is empty"

        for laptop in laptops:
            if isinstance(laptop, Laptop):
                s += "\n" + str(laptop)

        return s


import random
import string
from human import Human


# генерация людей - это функциональный класс
class HumanCreator:

    @staticmethod
    def create(size):
        NAMES = ("Alex", "Kate", "Mary", "Alice", "Peter", "Ivan",
                 "Vladimir", "Matvey", " Max", "Victor")  # tuple

        MAX_AGE = 130
        MIN_AGE = 0

        ALFABET = string.ascii_uppercase  # вместо фамилии исплользовать букву

        ls = []

        for _ in range(size):
            firstname = random.choice(NAMES)  # метод choice
            surname = ALFABET[random.randrange(len(ALFABET))]
            age = random.randint(MIN_AGE, MAX_AGE)
            alive = random.randrange(2)  # должно выдаваться 2 стотяния 0 или 1

            human = Human(firstname, surname, age, alive)

            ls.append(human)

        return ls
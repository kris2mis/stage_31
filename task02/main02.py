from human import Human  # импорт из пакета
from analyst import Analyst
from creator import HumanCreator
from convertor import Convertor


def main():
    ls = HumanCreator.create(5)
    print(Convertor.convert_to_string(ls))

    count_adult = Analyst.count_adults(ls)
    count_alive = Analyst.count_alive_people(ls)

    print(f"Count of adults: {count_adult}")
    print(f"Count of alive: {count_alive}")


if __name__ == "__main__":
    main()
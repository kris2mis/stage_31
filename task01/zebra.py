# Необходимо реализовать программный компонент, эмулирующий зебру
# (zebra). Данный компонент должен иметь небольшое поведение в виде ме-
# тода get_stripe(), который исходя из внутреннего состояния объект должен
# выдавать последовательно или строку «black line» (чёрная полоска), или
# строку «white line» (белая полоска) при своём однократном вызове на зебра-
# объекте. Метод после создания объекта всегда должен первым выдавать
# строку «black line». Далее необходимо написать небольшую программу, ко-
# торая бы создавала пару зебр-объектов и демонстрировала работу основ-
# ного поведения данных объектов

#не получилось избавиться от none

class Zebra:
    def __init__(self, count=0):
        self._count = count
        # self._count += 1

    def get_stripe(self):
        if self._count == 0:
            # print("black line")
            result ="black line"
        elif self._count % 2 == 0:
            result = "black line"
        else:
            result = "white line"
        self._count += 1
        return result


str1 = Zebra()

print(str1.get_stripe())
print(str1.get_stripe())
print(str1.get_stripe())


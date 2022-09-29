import math  # импортируем библиотеку чтобы считать синусы
import numpy  # штука для создания массива для графика
import matplotlib.pyplot as mpp  # библеотека для построения/вывода графика
if __name__ == '__main__':  # честно говоря не знаю как это работет
    arguments = numpy.arange(0, 200, 0.1)  # создаём массив - ось x для графика от 0 до 200 с шагом в 0.1
    mpp.plot(  # строим график
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]  # находим значения y для раннее созданного графика
        )
    mpp.show()  # выоводим график

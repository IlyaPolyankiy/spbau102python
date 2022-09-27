import math #импортируем библиотеку чтобы считать синусы
import numpy #штука для создания массива для графика
import matplotlib.pyplot as mpp #библеотека для построения/вывода графика
if __name__ == '__main__': #честно говоря не знаю как это работет
    arguments = numpy.arange(0, 200, 0.1) #создаём массив-график а аргументами от 0 до 200 с шагом в 0.1
    mpp.plot
    (
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments] #задаём формулу для заполнения графика
    )
    mpp.show() #вывод графика

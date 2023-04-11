import random

def count_pi(n):
    count = 0
    incircle = 0
    while count < n:
        # Генерируем координаты точки
        x = random.random()  
        y = random.random()
        # Если квадарт длины (следовательно сама длина) меньше 1, то точка лежит внутри окружности
        if 1>x*x+y*y:  
            incircle += 1
        count += 1
    PI = 4 * incircle / count  # Мы рассматривали только первую четверть круга
    return PI

print(count_pi(100000))

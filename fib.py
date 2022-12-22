import itertools

first_2_fibs = [1, 1]

class Fibs:
    """По объектам этого класса можно итерироваться и получать числа Фибоначчи"""
    class _FibNum_iter:
        """Внутренний класс — итератор"""
        def __init__(self):
            self.i = 0
            self.fibs = first_2_fibs

        def __next__(self):
            j = self.i
            self.i += 1
            x = self.fibs[j] + self.fibs[j + 1]
            self.fibs.append(x)
            return self.fibs[j]

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fibs._FibNum_iter()


fb = Fibs()
n = int(input("Введите кол-во чисел фибоначчи: "))
for i, f in zip(
    itertools.count(1),
    itertools.islice(fb, n)
):
    print(i, f)

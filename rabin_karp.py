"""
Реализация алгоритма Рабина-Карпа с модульными тестами
"""

import unittest

def rabin_karp(text, pattern):
    patlen = len(pattern)
    textlen = len(text)
    pathash = 0  
    texthash = 0    
    result = []
    if textlen == 0:  # если мы ищем в пустом тексте
        return []
    if patlen == 0:  # если мы ищем пустое слово
        return list(range(textlen))
    for i in range(patlen):  # считаем хэш искомой подстроки
        pathash = pathash + ord(pattern[i])
        texthash = texthash + ord(text[i])
    for i in range(textlen-patlen+1): 
        if pathash == texthash:  # если хэш текущей подстроки совпадает с хэшем искомой
            result += [i]        # добавляем номер элемента текста с которого начинается подстрока
        if i < textlen - patlen:
            texthash = texthash - ord(text[i]) + ord(text[i+patlen])  # рассчитываем хэш для подстроки, начинающейся со следующего элемента
    return result  # возвращаем список


class RabinKarpTest(unittest.TestCase):
    """Тесты для метода Рабина-Карпа"""

    def setUp(self):
        """Инициализация"""
        self.text1 = 'axaxaxax'
        self.pattern1 = 'xax'
        self.text2 = 'bababab'
        self.pattern2 = 'bab'

    def test_return_type(self):
        """Проверка того, что функция возвращает список"""
        self.assertIsInstance(
            rabin_karp(self.text1, "x"), list,
            msg="Функция должна возвращать список"
        )

    def test_returns_empty(self):
        """Проверка того, что функция, когда следует, возвращает пустой список"""
        self.assertEqual(
            [], rabin_karp(self.text1, "z"),
            msg="Функция должна возвращать пустой список, если нет вхождений"
        )
        self.assertEqual(
            [], rabin_karp("", self.pattern1),
            msg="Функция должна возвращать пустой список, если текст пустой"
        )
        self.assertEqual(
            [], rabin_karp("", ""),
            msg="Функция должна возвращать пустой список, если текст пустой, даже если образец пустой"
        )

    def test_finds(self):
        """Проверка того, что функция ищет все вхождения непустых образцов"""
        self.assertEqual(
            [1, 3, 5], rabin_karp(self.text1, self.pattern1),
            msg="Функция должна искать все вхождения"
        )
        self.assertEqual(
            [0, 2, 4], rabin_karp(self.text2, self.pattern2),
            msg="Функция должна искать все вхождения"
        )

    def test_finds_all_empties(self):
        """Проверка того, что функция ищет все вхождения пустого образца"""
        self.assertEqual(
            list(range(len(self.text1))), rabin_karp(self.text1, ""),
            msg="Пустая строка должна находиться везде"
        )

# Запуск тестов
if __name__ == '__main__':
    unittest.main()
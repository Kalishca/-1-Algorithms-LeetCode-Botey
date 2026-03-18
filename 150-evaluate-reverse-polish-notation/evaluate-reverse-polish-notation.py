from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Вычисляет значение арифметического выражения, заданного в обратной польской записи.
        Используется стек, реализованный на базе списка Python.
        """
        stack = []  # стек для операндов и промежуточных результатов

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # Извлекаем два верхних операнда
                b = stack.pop()  # правый операнд
                a = stack.pop()  # левый операнд

                if token == "+":
                    res = a + b
                elif token == "-":
                    res = a - b
                elif token == "*":
                    res = a * b
                else:  # token == "/"
                    # Деление с отсечением к нулю
                    res = int(a / b)  # int() отбрасывает дробную часть (truncate toward zero)

                stack.append(res)
            else:
                # Токен — число, преобразуем в int и помещаем в стек
                stack.append(int(token))

        # В стеке остаётся единственное значение — результат
        return stack[0]       
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []                     # инициализация стека
        # Словарь соответствий закрывающих скобок открывающим
        mapping = {')': '(', '}': '{', ']': '['}
        
        for ch in s:
            if ch in mapping:          # если символ — закрывающая скобка
                if not stack:          # стек пуст — нет пары
                    return False
                top = stack.pop()       # извлекаем верхний элемент
                if top != mapping[ch]:  # проверяем соответствие
                    return False
            else:                       # иначе это открывающая скобка
                stack.append(ch)        # кладём в стек
        
        return not stack                # стек должен быть пуст
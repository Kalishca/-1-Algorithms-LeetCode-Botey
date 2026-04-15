def get_frequencies(text):
    # Подсчет частоты символов
    freqs = {}
    for char in text:
        freqs[char] = freqs.get(char, 0) + 1
    return freqs

def huffman_encoding(text):
    # Функция кодирования Хаффмана
    if not text:
        return "", None
    # Создаем начальный список узлов
    # Узел = [частота, символ, левый, правый]
    freqs = get_frequencies(text)
    nodes = []
    for char, freq in freqs.items():
        nodes.append([freq, char, None, None])
    # Построение дерева
    while len(nodes) > 1:
        # Сортируем список по частоте (индекс 0)
        nodes.sort(key=lambda x: x[0])
        # Извлекаем два минимальных узла
        left = nodes.pop(0)
        right = nodes.pop(0)
        # Создаем родительский узел: частота = сумма частот
        # Символ у родителя = None
        parent = [left[0] + right[0], None, left, right]
        nodes.append(parent)
    root = nodes[0]
    # Генерация таблицы кодов
    codes = {}

    def build_codes(current_node, current_path):
        if current_node is None:
            return
        # Если это лист (есть символ в индексе 1)
        if current_node[1] is not None:
            codes[current_node[1]] = current_path
        #Рекурсия: влево (индекс 2) добавляем 0, вправо (индекс 3) добавляем 1
        build_codes(current_node[2], current_path + "0")
        build_codes(current_node[3], current_path + "1")

    build_codes(root, "")

    # Кодирование строки
    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, root

#Функция декодирования Хаффмана
def huffman_decoding(encoded_text, root):

    if not encoded_text or root is None:
        return ""

    decoded_output = ""
    current_node = root

    for bit in encoded_text:
        # Переход влево (2) или вправо (3)
        if bit == '0':
            current_node = current_node[2]
        else:
            current_node = current_node[3]

        # Проверка на лист (наличие символа)
        if current_node[1] is not None:
            decoded_output += current_node[1]
            current_node = root  # Возврат к корню

    return decoded_output


# Пример работы
text = "banana"
encoded, tree = huffman_encoding(text)
decoded = huffman_decoding(encoded, tree)

print(f"Текст: {text}")
print(f"Код: {encoded}")
print(f"Результат декодировки: {decoded}")
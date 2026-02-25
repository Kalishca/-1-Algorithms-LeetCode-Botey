def selection_sort(arr):
    """
    Сортировка выбором (по возрастанию).
    На каждом шаге находит минимальный элемент в неотсортированной части
    и меняет его с первым элементом этой части.
    """
    n = len(arr)
    # i - индекс начала неотсортированной части
    for i in range(n - 1):
        # Предполагаем, что первый элемент неотсортированной части минимальный
        min_index = i
        # Ищем реальный минимум в оставшейся части
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Если нашли элемент меньше текущего, меняем местами
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
test_array = [64, 25, 12, 22, 11]
print("Исходный массив:", test_array)
sorted_array = selection_sort(test_array)
print("Отсортированный массив:", sorted_array)
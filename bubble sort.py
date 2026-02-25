def bubble_sort_optimized(arr):
    """Сортировка пузырьком с оптимизацией (ранний выход при отсутствии обменов)."""
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # флаг: были ли обмены на этом проходе
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
        # Если обменов не было, массив уже отсортирован
        if not swapped:
            break
    return arr

# Проверка на примере
test_array = [1, 4, 1, 2, 4, 243, 0]
print("Исходный массив:", test_array)
sorted_array = bubble_sort_optimized(test_array)
print("Отсортированный массив:", sorted_array)
import random

def partition(arr, low, high):
    """Разбиение массива относительно случайного опорного элемента."""
    rand_pivot = random.randint(low, high)
    arr[rand_pivot], arr[high] = arr[high], arr[rand_pivot]
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_select(arr, k):
    """
    Возвращает k-й наименьший элемент в массиве arr (k начинается с 0).
    Массив может быть изменён в процессе работы.

    Почему алгоритм не сортирует весь массив?
    После разбиения (partition) опорный элемент оказывается на своей финальной позиции.
    В отличие от быстрой сортировки, которая рекурсивно обрабатывает обе части,
    quick_select идёт только в ту половину, где находится искомый индекс k.
    Это означает, что на каждом уровне рекурсии обрабатывается только один подмассив,
    размер которого в среднем уменьшается вдвое.

    Как это влияет на сложность?
    Суммарное количество операций примерно равно n + n/2 + n/4 + ... < 2n,
    поэтому средняя временная сложность составляет O(n).
    В худшем случае (например, при систематически неудачном выборе опорного)
    сложность может вырасти до O(n²), но случайный выбор опорного элемента
    минимизирует вероятность этого.
    """
    def _quick_select(low, high):
        if low == high:
            return arr[low]
        pivot_index = partition(arr, low, high)
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return _quick_select(low, pivot_index - 1)
        else:
            return _quick_select(pivot_index + 1, high)

    return _quick_select(0, len(arr) - 1)


# Пример использования
arr = [3, 6, 1, 8, 2, 5]
k = 2  # ищем 3-й наименьший (индекс 2)
result = quick_select(arr.copy(), k)  # используем копию, чтобы сохранить оригинал
print(f"{k+1}-й наименьший элемент: {result}")
print(f"Проверка (отсортированный массив): {sorted(arr)}")
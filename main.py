import random
#from typing import List


def mas(n: int) -> list:
    """
    Функция заполнения массива
    :param n: Длина массива
    :return: Заполненный массив случайными элементами
    """
    list1 = []
    for i in range(0, n):
        list1.append(random.randint(-100, 100))
    return list1

def max_min(list_: list) -> max and min:
    """
    Функция поиска и минимума в списке
    :param list_: На вход поступает список из n элементов
    :return: Возвращается максимальный и минимальный элемент из списка
    """
    max = 0
    min = list_[0]
    for i in range(len(list_)):
        if list_[i] > max:
            max = list_[i]
        if list_[i] < min:
            min = list_[i]
    return print(f'максимум = {max}\nминимум = {min}')

def bubble_sort(list_: list) -> list:
    """
    Функция принимает массив и сортирует в порядке возрастания методом пузырька
    :param list_: Список
    :return: Отсортированный список в порядке возрастания
    """
    for i in range(len(list_)-1):
        for j in range(len(list_)-1):
            if list_[j] > list_[j+1]:
                list_[j], list_[j+1] = list_[j+1], list_[j]
    return list_

def selection_sort(list_: list) -> list:
    """
    Сортировка выборкой
    :param list_: Список
    :return: Отсортированный список
    """
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(list_)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(list_)):
            if list_[j] < list_[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        list_[i], list_[lowest_value_index] = list_[lowest_value_index], list_[i]
    return list_

def insertion_sort(list_: list) -> list:
    """
    Сортировка вставками
    :param list_: Список
    :return: отсортированный список
    """
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(list_)):
        item_to_insert = list_[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and list_[j] > item_to_insert:
            list_[j + 1] = list_[j]
            j -= 1
        # Вставляем элемент
        list_[j + 1] = item_to_insert
    return list_

def merge_sort(list_: list) -> list:
    """
    Сортировка слиянием
    Рекурсивный алгоритм, который работает по следующему принципу:
        1) Разделить массив на две равные части
        2) Отсортировать каждую половину
        3) Из двух отсортированных массивов получить один (операция слияния)
    :param list_: Список
    :return: Отсортированный список
    """
    # Возвращаем список, если он состоит из одного элемента
    if len(list_) <= 1:
        return list_

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(list_) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(list_[:mid])
    right_list = merge_sort(list_[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)

def merge(left_list, right_list): # Сортировка слиянием
    """
    Сортировка левой и правой части списка
    :param left_list: Левая часть списка
    :param right_list: Правая часть списка
    :return: Отсортированный спиоск
    """

    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort_2(list_: list) -> list:
    """
    Сортировка слиянием второй вариант исполнения
    :param list_: Список
    :return: Отсортированный список
    """
    if len(list_) > 1:
        mid = len(list_) // 2 # разделить список надвое
        left = list_[:mid] # формирование левого списка
        right = list_[mid:] # формирование правго списка
        merge_sort_2(left)
        merge_sort_2(right)
        """
        i — индекс в списке left,
        j — индекс в списке right,
        k — индекс в исходном списке list_, в который в конечном итоге
        нужно вставить все числа по порядку.
        
        Если число из списка left меньше, чем число из списка right, 
        мы вставляем его в list_ на позицию k, после чего увеличиваем индекс i на единицу. 
        Если число из списка right меньше или равно числу из списка left, 
        тогда оно отправляется в list_, а мы увеличиваем на единицу индекс j. 
        Наконец, после добавления любого из чисел в список list_, 
        мы увеличиваем на единицу индекс k.
        """
        i = j = k = 0
        while i < len(left) and j < len(right): # если эти условия выполняются, цикл прерывается
            if left[i] < right[j]:
                list_[k] = left[i]
                i += 1
            else:
                list_[k] = right[j]
                j += 1
            k += 1
            """
            если мы дойдем до конца списка left, а в списке right еще останутся элементы?
            На этот случай нам нужно сделать еще один цикл while.
            В этом цикле мы будем перебирать остаток элементов в списке right и добавлять их в список list_. 
            То же самое мы сделаем и для списка left.
            """
            while j < len(right):
                list_[k] = right[j]
                j += 1
                k += 1
            while i < len(left):
                list_[k] = left[i]
                i += 1
                k += 1


def quick_sort(list_: list) -> list:
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # Это индекс после разворота, где наши списки разделены
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(list_, 0, len(list_) - 1)

def partition(list_, low, high):
    """
    Функция раздела списка
    :param list_: Список
    """
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = list_[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while list_[i] < pivot:
            i += 1

        j -= 1
        while list_[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        list_[i], list_[j] = list_[j], list_[i]


if __name__ == '__main__':
    n = int(input("Введите длину массива = "))
    sort_temp_arr = mas(n).copy()
    print(sort_temp_arr)
    max_min(sort_temp_arr)
    bubble_sort(sort_temp_arr)
    print(f"Cортировка пузырьком:\n{sort_temp_arr}")
    selection_sort(sort_temp_arr)
    print(f"Cортировка выборкой:\n{sort_temp_arr}")
    insertion_sort(sort_temp_arr)
    print(f"Cортировка вставками:\n{sort_temp_arr}")
    merge_sort(sort_temp_arr)
    print(f"Cортировка слиянием:\n{sort_temp_arr}")
    quick_sort(sort_temp_arr)
    print(f"Быстрая сортировка:\n{sort_temp_arr}")
    merge_sort_2(sort_temp_arr)
    print(f"Cортировка слиянием_2:\n{sort_temp_arr}")

    # mid = len(sort_temp_arr)   # разделить список надвое
    # left = sort_temp_arr[:mid]  # левый список
    # right = sort_temp_arr[mid:]  # правый список
    # print(f'середина {mid}')
    # print(f' левый  {left}')
    # print(f' правый  {right}')
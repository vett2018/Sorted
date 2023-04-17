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




if __name__ == '__main__':
    n = int(input("Введите длину массива = "))
    sort_temp_arr = mas(n).copy()
    print(sort_temp_arr)
    max_min(sort_temp_arr)
    bubble_sort(sort_temp_arr)
    print(f"Cортировка пузырьком:\n{sort_temp_arr}")
    selection_sort(sort_temp_arr)
    print(f"Cортировка выборкой:\n{sort_temp_arr}")
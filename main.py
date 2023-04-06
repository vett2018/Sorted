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

if __name__ == '__main__':
    n = int(input("Введите длину массива = "))
    new_arr = mas(n).copy()
    print(new_arr)
    max_min(new_arr)
    bubble_sort(new_arr)
    print(new_arr)


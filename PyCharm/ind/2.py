#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    a = list(map(int, input("введите элементы ").split()))

    # находим сумму положительных элементов
    summa = sum(i for i in a if i > 0)

    # для нахождения произведения между
    # макс и мин эл по модулю
    a_min = a_max = a[0]
    i_min = i_max = 0
    for i, item in enumerate(a):
        if math.fabs(item) < math.fabs(a_min):
            a_min, i_min = item, i
        if math.fabs(item) >= math.fabs(a_max):
            a_max, i_max = item, i

    # Проверить индексы и обменять их местами.
    if i_min > i_max:
        i_min, i_max = i_max, i_min

    # произведение
    pr = 1
    for item in a[i_min+1:i_max]:
        pr *= item

    print(f"сумма положительных элементов равна {summa}\nпроизведение между мин и макс эл-ми равно {pr}")

    # сортировка по убыванию
    a.sort(reverse=True)
    print(a)

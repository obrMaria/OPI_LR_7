#!/isr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    A = list(map(int, input("оценки по алгебре ").split()))
    G = list(map(int, input("оценки по геометрии ").split()))
    F = list(map(int, input("оценки по физике ").split()))

    # находим среднее значение успеваемости по алгебре
    sr_A = 0
    for i, item in enumerate(A):
        sr_A += item
    sr_A /= len(A)

    # находим среднее значение успеваемости по физике
    sr_F = 0
    for i, item in enumerate(F):
        sr_F += item
    sr_F /= len(F)

    # находим среднее значение успеваемости по геометрии
    sr_G = 0
    for i, item in enumerate(G):
        sr_G += item
    sr_G /= len(G)

    # определяем предмет с лучшей успеваемостью
    max_sr = max(sr_A, sr_G, sr_F)
    if max_sr == sr_A:
        print("по алгебре лучшая упеваемость =", sr_A)
    if max_sr == sr_F:
        print("по физике лучшая упеваемость =", sr_F)
    if max_sr == sr_G:
        print("по геометрии лучшая упеваемость =", sr_G)




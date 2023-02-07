# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.

import random


def generate_matrix():
    number = random.randint(0, 10)
    lst = [[random.randint(0, 10) for _ in range(number)] for _ in range(number)]
    answer = iter(lst)
    print("Вывод изначальной квадратной матрицы: ")
    while True:
        try:
            one = next(answer)
            print(*one)
        except StopIteration:
            print("Конец итерации. \n")
            break
    print("Вывод изменённой квадратной матрицы: ")
    answer_two = iter(lst)
    chet = 0  # Счетчик
    while True:
        try:
            two = next(answer_two)
            for k in range(number):
                if k != chet:
                    two[k] *= 2
            print(*two)
            chet += 1
        except StopIteration:
            print("Конец.")
            break


generate_matrix()

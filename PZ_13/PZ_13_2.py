# Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.

import random


def generate_matrix():
    number = random.randint(1, 8)
    lst = [[random.randint(-50, 90) for _ in range(number)] for _ in range(number)]

    answer = iter(lst)

    print("Вывод изначальной матрицы: ")
    flag = False
    while True:
        try:
            one = next(answer)
            for i in one:
                if i > 0:
                    flag = True
            print(*one)
        except StopIteration:
            print("Конец. \n")
            break
    print(f"В матрице имеются положительные элементы: {flag}")


generate_matrix()

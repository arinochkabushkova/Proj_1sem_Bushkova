# В последовательности на n целых чисел умножить элементы до n-1 на элемент n.

from random import randint

n = int(input("Введите длину последовательности: "))
list_n = []
for i in range(n):
    list_n.append(randint(-50, 50))
list_n_1 = [i * n for i in list_n[:n - 1]]
print(list_n)
print(list_n_1)

#Дан список размера N. Переставить в обратном порядке элементы список,
#расположенные между его минимальным и максимальным элементами, включая
#минимальный и максимальный элементы.

from random import randint

while True:
    try:  # обработка исключений
        N = int(input('Введите длинну списка: '))  # Ввод числа
        break
    except ValueError:
        print("Не корректный ввод, попробуйте еще раз!")

lint = [randint(0, 100) for i in range(N)]
print('Исходный список: ', lint)  # вывод исходного списка
ind_min = lint.index(min(lint))  # используем функцию min
ind_max = lint.index(max(lint))  # используем функцию max
interval = lint[ind_min:ind_max + 1][::-1]
del lint[ind_min:ind_max + 1]
i = ind_min
j = 0
while i < ind_max + 1: # цикл если i < индекса max
    lint.insert(i, interval[j]) # добавляем указанный элемент в список
    i += 1
    j += 1

print('Результат: ', lint)

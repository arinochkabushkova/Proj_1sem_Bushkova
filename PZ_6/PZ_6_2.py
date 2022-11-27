#Дан список размера N. Найти номер его последнего локального максимума
#"(локальный максимум — это элемент, который больше любого из своих соседей).


from random import randint

while True:
    try:  # обработка исключений
        N = int(input('Введите длинну списка: '))  # Ввод числа
        break
    except ValueError:
        print("Не корректный ввод, попробуйте еще раз!")

list_int = [randint(0, 101) for i in range(N)]
for i in list(range(N))[::-1]: # цикл for с последовательностью до N
    if list_int[i] < list_int[i - 1] > list_int[i - 2]:
        print(list_int[i - 1]) # вывод списка
        break

# Дано вещественное число - цена 1 кг конфет. Вывести стоимость 1, 2, …, 10 кг конфет.


while True:
    try:  # обработка исключений
        a = float(input('Введите цену за 1 кг конфет: '))  # Ввод числа
        break
    except ValueError:
        print("Не корректный ввод, попробуйте еще раз!")

i = 0.1
while i <= 1:  # цикл вычисления стоимости
    print(f'Стоимость конфет за {round(i, 2)} кг - {round(a * i, 2)}')  # вывод стоимости конфет
    i += 0.1

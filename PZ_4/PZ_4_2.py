# Дано целое число N (> 0). Используя операцию  деления нацело и взятия остатка от деления, найти число, полученное
# при прочтении числа N справа налево.

while True:
    try: # обработка исключений
        N = int(input('Введите N: ')) # Ввод числа
        if N > 0:
            break
        else:
            raise ValueError
    except ValueError:
        print("Не корректный ввод, попробуйте еще раз!")
resalt = 0
while N != 0:
    resalt *= 10
    resalt += int(N % 10)
    N = int(N / 10)

    print(resalt)

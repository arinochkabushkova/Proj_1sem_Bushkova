# Описать функцию RectPS(x1, x2, y1, y2, P, S), вычисляющую периметр P и площадь S прямоугольника со сторонами,
# параллельными осям координат, по координатам (x1, y1), (x2, y2) его противоположных вершин (x1, x2, y1,
# y2 - входные, P и S - выходные параметры вещественного типа). с помощью этой функции найти периметры и площади трех
# прямоугольников с данными противоположными вершинам.

def RectPS(x1, y1, x2, y2, Res):  # функция вычисления периметра и площади прямоугольника
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    print("a = ", a)
    print("b = ", b)
    Res['P'] = 2 * (a + b)
    Res['S'] = a * b
    return


x1, x2, y1, y2 = input("Введите X1: "), input("Введите X2:"), \
                 int(input("Введите Y1: ")), input("Введите Y2:")  # ввод вещественных чисел

while type(x1) != float:  # обработка исключений
    try:
        x1 = float(x1)
    except ValueError:
        print('Не корректный ввод, попробуйте ещё раз!')
        x1 = input('Введите X1: ')
while type(x2) != float:  # обработка исключений
    try:
        x2 = float(x2)
    except ValueError:
        print('Не корректный ввод, попробуйте ещё раз!')
        x2 = input('Введите X2: ')
while type(y1) != float:  # обработка исключений
    try:
        y1 = float(y1)
    except ValueError:
        print('Не корректный ввод, попробуйте ещё раз!')
        y1 = input('Введите Y1: ')
while type(y2) != float:  # обработка исключений
    try:
        y2 = float(y2)
    except ValueError:
        print('Не корректный ввод, попробуйте ещё раз!')
        y2 = input('Введите Y2: ')

R = {'P': None, 'S': None}  # словарь
RectPS(x1, y1, x2, y2, R)  # вызов функции RectPS
print('P = ', R['P'])  # вывод приметра прямоугольника
print('S = ', R['S'])  # вывод площади прямоугольника

# Скорость первого автомобиля Vi км/ч, второго — V2 км/ч, расстояние
# между ними S км. Определить расстояние между ними через T часов, если автомобили
# удаляются друг от друга. Данное расстояние равно сумме начального расстояния и общего
# пути, проделанного автомобилями; общий путь = время • суммарная скорость.
u1 = int(input("Введите скорость 1 "))  # Вводим скорость u1
u2 = int(input("Введите скорость 2 "))  # Вводим скорость u2
S = int(input("Введите расстояние "))  # Вводим расстояние S
T = int(input("Введите время "))  # Вводим время T
P = abs(S - ((u1 + u2) * T))  # Рассчитываем расстояние между автомобилями через T часов
print("Расстояние между ними через T часов= ", P)

#Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы
#неравенства A > 2 и B < 3».
while True: # обработка исключений
  try:
    a = int(input("Введите число а: ")) # ввод целого числа a
    b = int(input("Введите число b: ")) # ввод целого числа b
    break
  except:
      print('Ошибка, введите число')

print(bool(a > 2 and b < 3)) # вывод True или False

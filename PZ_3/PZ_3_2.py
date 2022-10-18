while True:
  try:
     a = int(input("Введите Длину волны: "))
     break
  except:
    print('Ошибка, введите число')

if a <= 450:
 print('Фиолетовый')
elif 450 <= a <= 480:
 print('Синий')
elif 480 <= a <= 510:
 print('Сине-зеленый')
elif 510 <= a <= 550:
 print('Зеленый')
elif 550 <= a <= 570:
 print('Желто-Зеленый')
elif 570 <= a <= 590:
 print('Желтый')
elif 590 <= a <= 630:
 print('Оранжевый')
elif 630 >= a:
 print('Красный')
else:
  print('Длинна волны вне диапазона видимых волн!')
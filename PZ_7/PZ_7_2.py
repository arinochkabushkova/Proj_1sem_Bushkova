# Дана строка-предложение. Зашифровать ее, поместив вначале все символы,
#расположенные на четных позициях строки, а затем, в обратном порядке, все
#символы, расположенные на нечетных позициях (например, строка «Программа»
#превратится в «ргамамроП»).
s = input('Введите строку-предложение: ')
print('Оригинальное предложение: ', s)
print('Зашифрованное предложение: ', s[::2] + s[1::2][::-1])
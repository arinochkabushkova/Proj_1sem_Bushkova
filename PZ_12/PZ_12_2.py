# Составить генератор (yield), который выводит из строки только буквы

def get_string(gen_lst):
    yield [i for i in gen_lst if i.isalpha()]


st = input("Введите данные: ")
answer = get_string(st)
print(*list(answer))

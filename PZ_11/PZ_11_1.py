import random

f = open('file_int.txt', 'w')
f.write(' '.join([str(random.randint(-40, 40)) for i in range(50)]))
f.close()
f = open('file_int.txt', 'r')
data = f.read().split(' ')
a = [int(i) for i in data]
for i in range(len(a) - 1):
    if (a[i]) < a[i + 1] + 1:
        first_max_elem = a[i + 1]
        break
f.close()
f = open('file_int.txt', 'w')
f.write(f'Исходные данные - {data}\n')
f.write(f'Количество элементов - {len(data)}\n')
f.write(f'Минимальный элемент - {min(a)}\n')
f.write(f'Элементы, умноженные на первый максимальный элемент - {[i * first_max_elem for i in a]}\n')

f.close()
# Найти сумму элементов первой и второй половины словаря


def sum_dict(dict_element: dict):
    value_dict = list()
    for i in list(dict_element.items()):
        value_dict.append(i[-1])
    return f'Суммы первой половины: {sum(value_dict[:int(len(value_dict) / 2)])}\n' \
           f'Сумма второй половины: {sum(value_dict[int(len(value_dict) / 2):])}'


print(sum_dict({'one': 1, 'two': 2, 'three': 3, 'four': 4}))  # ввести словарь с четным кол-вом элементов

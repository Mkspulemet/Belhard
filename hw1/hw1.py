import re


def my_tuple():
    try:
        my_tuple = input("Введите четыре числа через пробел: ")
        my_tuple = re.findall(r'\d+', my_tuple)
        if len(my_tuple) != 4:
            raise ValueError("Нужно ввести ровно 4 числа")
        my_tuple = tuple(map(int, my_tuple))
        message = {"тип данных": type(my_tuple), "весь кортеж": my_tuple, "второй элемент": my_tuple[1]}
        return message
    except Exception as e:
        return e

if __name__ == '__main__':
    print(my_tuple())
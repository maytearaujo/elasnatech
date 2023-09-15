def somar():
    print('Está função soma valores')


def mult():
    print('Está função multiplica valores')


def find_index(to_find, item):
    for  i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1
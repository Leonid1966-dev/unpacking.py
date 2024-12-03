def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(4, 'море', False)
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(58, 'поле', False)
print_params(1236, 'дорога')
print_params(b = 'работа')
print_params(b = 25)
print_params(c = [1, 2, 3])


values_list = [58, 'почва', False]
values_dict = {'a': 500, 'b': 'ключ', 'c': True}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [58.5, 'ноутбук']
print_params(*values_list_2, 42)



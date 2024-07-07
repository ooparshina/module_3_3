def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

#задача1
print_params(b = 25)
print_params(c = [1,2,3])

#задача2
values_list = ['один', 14, [1, 2, 3]]
values_dict = {'a': 30, 'b': 34, 'c': 5}
print_params(*values_list)
print_params(**values_dict)

#задача3
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
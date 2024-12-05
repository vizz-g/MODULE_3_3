def print_params(a=1, b='qwert', c=True):
    print(a, b, c)


print_params(2, 'qwe')
print_params(4, None, True)
print_params(4562)
print_params([1, 2, 3], 'trewq')
print_params()
print_params(b=25)
print_params(c={1, 2, 3})

values_list_2 = [40, 'qwer']
print_params(*values_list_2, 42)

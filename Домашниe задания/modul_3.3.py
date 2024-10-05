def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1,2,3])

values_list = ['дом', 'Good', 74567]
values_dict = {'a':6765, 'b':7694, 'c':87497}

print_params(*values_list)
print_params(**values_dict)

values_list2 = [False, 78.54]

print_params(*values_list2)
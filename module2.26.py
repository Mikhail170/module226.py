# def print_params(a=1, b='string', c=True):
#     print(a, b, c)
#
#
# print_params()
# print(1, 2, 3)
# print(1, 2)
#
# print(print_params(b=25, c=[1, 2, 3]))
# #rint(a=True, b=25, c=[1, 2, 3])
#
# def print_params(a, b, c):
#     print(a, b, c)
#
#
# values_list = [1, True, 'string']
# values_dict = {'a': 1, 'b': True, 'c': [1, 2, 3]}
#
# print_params(*values_list)
# print_params(**values_dict)

def print_params(a, b, c):
    print(a, b, c)


values_list2 = [54.32, 'String']
print_params(*values_list2, 42)
























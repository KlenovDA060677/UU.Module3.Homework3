# Самостоятельная работа по уроку "Распаковка позиционных параметров".

def print_params(a=1, b='Urban', c=True):
    '''Принимает три параметра со значениями по умолчанию
       a, b, c и выводит их на экран'''
    print(f'a = {a}, b = {b}, c = {c}')

# Вызов функции print_params с разным количеством и типом параметров
print_params()
print_params(b=25)
print_params(c=[1,2,3])
print_params(47, True, c='Дмитрий', )

values_list = [1,True,'Дмитрий']
values_list2 = [22, '33']
values_dict = {'a': True, 'b': 'Дмитрий', 'c': 47}
values_dict2 = {'b': 2, 'c': '3'}

# Вызов функции print_params с распаковкой сипсков и словарей
# в качестве именованных и неименованных параметров
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list2, 44)
print_params(1, **values_dict2)

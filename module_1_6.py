my_dict = {'Alex': 2000, 'Sonya': 1999, 'Valery': 2002}
my_dict ['Alex'] = 1998
my_dict ['Nikita'] = 1999
print(my_dict['Alex'])
print(my_dict.get('Nikolay'))
my_dict.update({'Petr': 2003,
               'Igor': 1963})
print(my_dict)
my_dict.pop('Alex')
print(my_dict)

my_set = {1, 2, 3, 4, 1, 2, 3, 4, 5, 'White'}
print(my_set)
my_set.update(['Six', 6])
print(my_set)
print(my_set.discard(2))
print(my_set)
print(my_set.remove('Six'))
print(my_set)
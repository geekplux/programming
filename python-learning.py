#!/usr/bin/env python



## print

print('\nHello World!')
print('1 * 9 + 1 =', 1 * 9 + 1)

print('please input something: ')
_str = input()
print('output', _str)

print('I\'m learning Python.\n\n')

## end print



## data type

print('Judge the data type:\n')
_varied_type_data = (None, [True, False], {1, 2, 3}, {1: 'hello', 2: 'world'}, 88, 'ABC')

print(type(_varied_type_data))

for var in _varied_type_data:
    print('{:<30} ==> {}'.format(str(var), type(var)))

## end data_type



## encoding

print('\n\nEncoding transform:\n')
print(ord('A'))
print(ord('汉'))
print(chr(65))
print(chr(ord('汉')))

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print(b'ABC'.decode('ascii'))
print('中文'.encode('utf-8').decode('utf-8'))

## encoding



## list tuple dict set

print('\n\nAbout list, tuple, dict, set:\n')

# list
languages_list = ['python', 'c', 'c++', 'java']
languages_list.append('javascript')
languages_list.insert(1, 'lisp')
languages_list.reverse()
languages_list.sort()
print(languages_list)

# tuple
languages_tuple = ('python', 'c', 'c++', 'java')
print(languages_tuple)

# dict
languages_dict = {'python': 1, 'c': 2, 'c++': 3, 'java': '4'}
languages_dict.pop('java')
print(languages_dict)
print(languages_dict['python'], languages_dict['c'])
print('python' in languages_dict)
print(languages_dict.get('python'))

#set
set_example = set([1, 1, 2, 2, 3, 3])
set_example.add(4)
print(set_example)
set_example_temp = set([4, 4, 5, 5, 6, 6, 7, 7])
print(set_example_temp)
print(set_example.difference(set_example_temp))
print(set_example.union(set_example_temp))
set_example_temp.clear()

## end list tuple dict set



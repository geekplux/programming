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



## control flow

print('\n\nAbout control flow:\n')

# choice: if-else statements
condition_true = True
condition_false = False
if condition_false:
    print('condition is false!')
elif condition_false and condition_true:
    print('condition is', condition_false and condition_true)
elif condition_true:
    print('condition is true!')
else:
    print('else condition')

# loops: for
sum = 0
for x in range(101):
    sum = sum + x
print('loops for:', sum)

# loops: while
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print('loops while:', sum)

print('\nitetate:\n')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

## end control flow



## function

def _abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print('abs:', _abs(10), _abs(-10))
# print(_abs('10')) # will throw a error

# variable arguments
def _sum_variable_arguments(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

print(_sum_variable_arguments(1, 2, 3, 4, 5))

# keywords arguments
def _people_info_keywords_arguments(name, gender, **kw):
    print('name:', name, 'gender:', gender, 'other:', kw)

_people_info_keywords_arguments('Mike', 'Male', job='developer')

## end function



## slice

_slice_list = list(range(100))
print(_slice_list[:])
print(_slice_list[::-1])
print(_slice_list[:10])
print(_slice_list[-10:])
print(_slice_list[-10::2])

## end slice



## range

print('generate list by range:\n')
print([x * x for x in range(1, 11) if x % 2 == 0])

_abc_dict = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in _abc_dict.items()])

_a_str_list = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in _a_str_list])

## end range

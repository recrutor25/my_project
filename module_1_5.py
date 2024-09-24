#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 21 09 2024
@author: igor
"""
print('К О Р Т Е Ж И','\n')
immutable_var = 1, 2, 3, True, "string"
print('Создание кортежа:       ',immutable_var )
print('ошибка                   immutable_var[1] = 45 ', '\n', 'Кортежи нe \
поддерживают изменение элементов','\n')

print('С П И С К И','\n')

mutable_list = [5, 8, 'apple', 'banana', False] #
print('Создание списка:        ',mutable_list )

mutable_list.reverse()
print('Обратная перестановка:  ', mutable_list)

mutable_list.extend(['cat', 'dog', 10 ])
print('Добавление элементов:   ', mutable_list)

mutable_list.pop(1)
print('Удаление по индексу:    ', mutable_list)

mutable_list[0] = True
print('Изменение по индексу:   ', mutable_list)


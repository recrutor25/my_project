#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 21 09 2024
@author: igor
"""
my_string = input("Введите слово: ")
print("Вы ввели символов: ", len(my_string))

print("Вывод строки в верхнем регистре: ", my_string.upper())
print("Вывод строки в нижнем  регистре: ", my_string.lower())
print("Удаление всех пробелов ", my_string.replace(' ',''))
print("Вывод первого символа: ", my_string[0])
print("Вывод последнего символа: ", my_string[-1])
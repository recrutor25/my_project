#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 22 09 2024
@author: igor
"""
print('     РАБОТА СО СЛОВАРЕМ:   ','\n')

my_car = {'brand': 'bmw', 'tip': 'седан', 'mileage': 58435}
print('вывод словаря на экран:                ', my_car,'\n')

tip = my_car['tip']
print('обращение по существующему  ключу:     ','тип кузова: ', tip )

my_car['tip_1'] = 'джип'
print('обращение по не существующему  ключу:  ','тип кузова: ', my_car[
    'tip_1'])
print('результат обращений:                   ', my_car, '\n')

my_car.update({'tip_2': 'пикап',
              'tip_3': 'микро автобус'})
print('добавление нескольких пар:             ', my_car)

print('удаление по ключу:', 'тип кузова ', my_car['tip_3'])
del my_car['tip_3']
print('результат удаления:                    ', my_car )

print('     РАБОТА С МНОЖЕСТВАМИ:   ','\n')



#my_car["tip_2"] = ""
#my_car[""] = ""
#dict_sample["Capacity"] = "1800CC"



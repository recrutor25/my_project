#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20 09 2024
@author: igor
"""
count_work = 12   # количество работ
count_time = 1.5  # затраченное время
course_name = 'Python' # название курса
time_task = count_time / count_work # среднее время выполнения

# 1 вариант
print('Курс: ' + course_name + ', всего задач:', count_work, 'затрачено \
часов:', count_time, 'среднее время выполнения', time_task, 'часа')

# 2 вариант
print('Курс:', course_name, ', всего задач:', count_work, 'затрачено \
часов:', count_time, 'среднее время выполнения', time_task, 'часа')

''' 
второй вариант выглядит криво а в первом сложение не работает с int()
и надо делать костыль для перевода в string интересно почему так 
или f строки нам в помощь 
'''
# 3 вариант
print('Курс: ' + course_name + ', всего задач: ' + str(count_work) + \
' затрачено часов: ' + str(count_time) + ' среднее время выполнения ' + \
str(time_task) + ' часа')
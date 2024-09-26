#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 22 09 2024
@author: igor
"""

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_list = sorted(list(students)) # сортируем список по алфавиту
# print(student_list)

middl_grades_list = [(sum(grades[0]) / len(grades[0])),(sum(grades[1]) / len(
    grades[1])),(sum(grades[2]) / len(grades[2])),(sum(grades[3]) / len(
    grades[3])), (sum(grades[4]) / len(grades[4]))]  # вычисляем средний бал
# print(grades_middl_list)

middl_grades_dict = dict(zip(student_list, middl_grades_list)) # совмещаем
# списки в соответствии с индексом

print(middl_grades_dict) #len(grades[3])),
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 14:51:33 2021

@author: stefano
"""

import datetime

class Person:

    def __init__(self, name, surname, birthdate):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age
    
    def __str__(self):
        return "My name is {} and I am {} years old.".format(self.name,str(self.age()))

"""
person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)
"""
#print(person.name)
#print(person.age())
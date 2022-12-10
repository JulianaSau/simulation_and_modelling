# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 11:40:14 2022

@author: waweru, Juliana Sau
"""
#The Automobile class holds general data
#about an automobile in inventory.

import math
import random
from turtle import *

colors = {
    1: 'white',
    2: 'silver',
    3: 'red',
    4: 'yellow',
    5: 'orange',
    6: 'brown',
    7: 'gray',
}

class Automobile:
    #The __init__ method accepts arguments for the
    #make, model, milieage, and price. It initializes
    #the data attributes with these values.

    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        self.a = 0
        self.b = 0.2 * math.pi
        self.scale = 1
        self.x = 0
        self.y = 0
        self.randlabel, self.randvalue = random.choice(list(colors.items()))

    #The following methods are mutators for the
    #class's data attributes.

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    #The following methods are the accessors
    #for the class's data attributes.

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price
    
    def random_number_gen(self):
        rand = random.random()
        return self.a + (rand * (self.b - self.a))

    def my_setpos(self, x_offset, y_offset):
        goto(self.x + self.scale*x_offset, self.y + self.scale*y_offset)

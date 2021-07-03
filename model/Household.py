# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:24:44 2021

@author: stefano
"""

from model.Person import Person
from model.Appliance import Appliance
import datetime
from matplotlib import pyplot as plt
import numpy as np

class HouseHold(Person):
   
    def __init__(self, name, surname, birthdate):
        Person.__init__(self, name, surname, birthdate)
        self.name = name
        self.list_appliances = []
        #self.wallet = Wallet()
        
    def add_appliance(self,appliance):
        
        self.list_appliances.append(appliance)

    def get_total_power(self):
        
        tot_power = 0
        for app in self.list_appliances:
            tot_power += app.nominal_power
        return tot_power

    def set_consumption_profile(self):
        for app in self.list_appliances:
            app.set_consumption_profile()

    def get_total_consumption_profile(self):
        tot_profile = np.zeros((24*6))
        for app in self.list_appliances:
            tot_profile = np.add(np.array(app.consumption_profile)*app.nominal_power,tot_profile)
            
        return tot_profile
        
if __name__ == "__main__":
    hh = HouseHold("ste","pasto",datetime.datetime(1987,7,13))
    new_app = Appliance("hair_dryer",2000)
    hh.add_appliance(new_app)
    new_app = Appliance("pc",200)
    hh.add_appliance(new_app)
    print(hh.list_appliances[0])
    hh.set_consumption_profile()
    plt.plot(hh.get_total_consumption_profile())
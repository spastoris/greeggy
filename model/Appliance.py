# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:26:13 2021

@author: stefano
"""

import datetime as dt
import random

class Appliance:
    """
    type_appliance - str
    id - int
    power - float
    energy_class - str
    flexibility - bool
    """
    
    def __init__(self, id, type_appliance, nominal_power, flexibility):
        self.id = id
        self.type_appliance = type_appliance
        self.power = power
        self.flexibility = flexibility

    """
    def __init__(self, which, nominal_power):
        list_of_appliances = ["air_conditioner","dish_washer","dryer",
                              "refrigerator","heater","boiler",
                              "washing_machine","microwave","oven",
                              "hair_dryer","tv","pc"]
        self.consumption_profiles = {}
        self.consumption_profiles["air_conditioner"]=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                                                 0.2, 0.4, 0.4, 0.4, 0.4, 0.4,
                                                 0.5, 0.5, 0.5, 0.5, 0.5, 0.8,
                                                 0.8, 0.8, 0.8, 0.6, 0.4, 0.3]
        self.consumption_profiles["dish_washer"]=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                             0.0, 0.0, 0.2, 0.2, 0.2, 0.2,
                                             0.5, 0.5, 0.5, 0.2, 0.2, 0.2,
                                             0.2, 0.5, 0.5, 0.5, 0.2, 0.2]
        self.consumption_profiles["dryer"]=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                       0.0, 0.0, 0.2, 0.2, 0.2, 0.2,
                                       0.5, 0.5, 0.5, 0.2, 0.2, 0.2,
                                       0.2, 0.5, 0.5, 0.5, 0.2, 0.2]
        self.consumption_profiles["heater"]=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                                        0.2, 0.4, 0.4, 0.4, 0.4, 0.4,
                                        0.5, 0.5, 0.5, 0.5, 0.5, 0.8,
                                        0.8, 0.8, 0.8, 0.6, 0.4, 0.3]
        self.consumption_profiles["boiler"]=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                                        0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                                        0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                                        0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
        self.consumption_profiles["refrigerator"]=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                                              0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                                              0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                                              0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
        self.consumption_profiles["washing_machine"]=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                 0.0, 0.0, 0.2, 0.2, 0.2, 0.2,
                                                 0.5, 0.5, 0.5, 0.2, 0.2, 0.2,
                                                 0.2, 0.5, 0.5, 0.5, 0.2, 0.2]
        self.consumption_profiles["microwave"]=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                           0.3, 0.5, 0.3, 0.2, 0.2, 0.2,
                                           0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                                           0.5, 0.5, 0.5, 0.2, 0.2, 0.0]
        self.consumption_profiles["oven"]=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                      0.3, 0.5, 0.3, 0.2, 0.2, 0.2,
                                      0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                                      0.5, 0.5, 0.5, 0.2, 0.2, 0.0]
        self.consumption_profiles["hair_dryer"]=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                            0.3, 0.5, 0.3, 0.2, 0.2, 0.2,
                                            0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                                            0.5, 0.5, 0.5, 0.2, 0.2, 0.0]
        self.consumption_profiles["tv"]=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                    0.3, 0.5, 0.3, 0.2, 0.2, 0.2,
                                    0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                                    0.5, 0.5, 0.5, 0.8, 0.8, 0.0]
        self.consumption_profiles["pc"]=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                    0.3, 0.5, 0.3, 0.2, 0.2, 0.2,
                                    0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                                    0.5, 0.5, 0.5, 0.2, 0.2, 0.0]
        if which in list_of_appliances:
            self.which = which
            self.nominal_power = nominal_power
        else:
            raise ValueError("{} is not in the list of appliances".format(which))
        self.working = False
    """    
    def set_consumption_profile(self):
        time = dt.datetime(2021,1,1,0,0,0)
        profile=[]
        for i in range(24*6):
            time+=dt.timedelta(0,600)
            prob = self.consumption_profiles[self.which][time.hour]
            choice = random.choices([True,False], weights = [prob, 1-prob])
            profile.append(choice)
        self.consumption_profile = profile

    def turn_on(self):
        self.working = True

    def turn_off(self):
        self.working = False
        
    def __str__(self):
        return "I am a {} and my nominal power is {} W".format(self.which,
                                                             str(self.nominal_power))
    
if __name__ == "__main__":
    fridge = Appliance(1,"FRIDGE",500.,True)

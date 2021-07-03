# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:50:14 2021

@author: stefano
"""

import datetime as dt
import random
import numpy as np
import matplotlib.pyplot as plt
from model.Household import HouseHold
from model.Appliance import Appliance

file_name = "C:/Users/stefa/Documents/greeggy/data/nomi_italiani.txt"
with open(file_name,"rb") as f:
    content = f.read()
    names = content.split()

power_per_appliance = {} #W
power_per_appliance["air_conditioner"] = 1500
power_per_appliance["dish_washer"] = 1500
power_per_appliance["dryer"] = 1200
power_per_appliance["refrigerator"] = 300
power_per_appliance["heater"] = 1500
power_per_appliance["boiler"] = 1000
power_per_appliance["washing_machine"] = 2000
power_per_appliance["microwave"] = 700
power_per_appliance["oven"] = 2000
power_per_appliance["hair_dryer"] = 2000
power_per_appliance["tv"] = 150
power_per_appliance["pc"] = 50

consumption_profile = [0.0239, 0.0191, 0.0144, 0.0096, 0.0096, 0.0096,
                       0.0574, 0.1053, 0.0718, 0.0287, 0.0191, 0.0478,
                       0.0574, 0.0383, 0.0239, 0.0096, 0.0239, 0.0478,
                       0.0718, 0.0813, 0.0766, 0.0718, 0.0478, 0.0335]


def random_profile():
    """Generate a random consumption profile"""

    cons_prof = np.array([i*random.uniform(0.8,1.2) for i in consumption_profile])
    norm = np.linalg.norm(cons_prof)
    cons_prof_n = cons_prof/norm

    return cons_prof_n

def random_date(start=dt.datetime(1950,1,1), end=dt.datetime(2000,1,1)):
    """Generate a random datetime between `start` and `end`"""
    return start + dt.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

def random_name(start, end):
    """Generate a random name from a list of names in a file"""

    return start + dt.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

def random_consumer():
    """Generate a random consumer profile"""

    basic_appliances = ["refrigerator","heater","boiler","washing_machine",
                        "oven","hair_dryer","tv","pc"]
    extra_appliances = ["air_conditioner","dish_washer",
                        "dryer","microwave"]
    name = random.choice(names)
    surname = random.choice(names)
    date = random_date()
    hh = HouseHold(name,surname,date)
    for app_name in basic_appliances:
        n = random.uniform(0.7,1.3)
        app = Appliance(app_name,int(power_per_appliance[app_name]*n))
        hh.add_appliance(app)
    for app_name in extra_appliances:
        if random.choice([True,False]):
            n = random.uniform(0.7,1.3)
            app = Appliance(app_name,int(power_per_appliance[app_name]*n))
            hh.add_appliance(app)
            
    hh.set_consumption_profile()
    
    return hh

def generate_population(n):
    list_household = []
    for elt in range(n):
        print(elt)
        list_household.append(random_consumer())
        
    tot_power_profile = np.zeros((24*6))
    for hh in list_household:
        tot_power_profile = np.add(np.array(hh.get_total_consumption_profile()),tot_power_profile)
            
    return tot_power_profile

if __name__ == "__main__":
    plt.plot(generate_population(5000))
    
    

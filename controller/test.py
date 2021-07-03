# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:50:14 2021

@author: stefano
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt


"""
for i in range(20):
    cons_prof = np.array([i*random.uniform(0.8,1.2) for i in consumption_profile])
    norm = np.linalg.norm(cons_prof)
    cons_prof_n = cons_prof/norm
    plt.plot(cons_prof)
"""
time = dt.datetime(2021,1,1,0,0,0)
profile=[]
for i in range(24*6):
    time+=dt.timedelta(0,600)
    time.hour
    prob = consumption_profiles["dish_washer"][time.hour]
    choice = random.choices([True,False], weights = [prob, 1-prob])
    profile.append(choice)

plt.plot(profile)

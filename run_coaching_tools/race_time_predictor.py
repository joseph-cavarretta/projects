# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:04:49 2020
@author: joseph
"""
########## RACE TIME PREDICTOR #################################################
LTpace = input("Threshold Pace ")
distance = float(input("Race Distance Miles "))
LTpercent = float(input("% of LT "))

## Convert pace to total time
split_pace = LTpace.split(":")
minutes = int(split_pace[0])
seconds = int(split_pace[1])
pace = minutes * 60 + seconds
racepace = pace * float(LTpercent)
totaltime = racepace * distance

hours = int(totaltime // 3600)
timeLeft = totaltime % 3600

minutes = int(timeLeft // 60)
seconds = int(timeLeft % 60)

print(f"\nRace Time = {str(hours)}:{str(minutes)}:{str(seconds)}")

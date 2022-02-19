# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:18:29 2021

@author: joe.cavarretta
"""
########## INPUT BASELINE LT VALUES ############################################
LTpwr = 300
LivingAlt = 5500

## Input Activity Data
AvgAlt = 11000
AvgPwr = 210

########## CALCULATE CHANGE IN LT BASED ON ALTITUDE ############################
AltConvert = ((((AvgAlt) - LivingAlt) / 500)/100)
AltLTpwr = (LTpwr*(1-AltConvert))

## Convert Activity Time to Seconds
time = '1:30:00'
split_time = time.split(':')
hours = int(split_time[0])
minutes = int(split_time [1])
seconds = int(split_time [2])
totsecs = (hours * 3600) + (minutes * 60) + seconds

## Calculate Baseline and Altitude Intensity Factor (IF)
IFpwr = AvgPwr / LTpwr
AltIFpwr = AvgPwr / AltLTpwr

########## CALCULATE TSS AND ALTITUDE TSS ######################################

## Absolute TSS
TSS = ((totsecs * AvgPwr * IFpwr)/(LTpwr * 3600) * 100)
print (f"Standard TSS = {round(TSS)}")

## Altitude TSS
AltTSS = ((totsecs * AvgPwr * AltIFpwr)/(AltLTpwr * 3600) * 100)
print (f"Altitude TSS = {round(AltTSS)}")

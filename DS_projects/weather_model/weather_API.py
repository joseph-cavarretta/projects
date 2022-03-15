# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 21:31:22 2022

@author: joseph
"""

from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Set time period
datetime.yesterday

# Create Point for Vancouver, BC
vancouver = Point(49.2497, -123.1193, 70)

# Get daily data for 2018
data = Daily(vancouver, start, end)
data = data.fetch()


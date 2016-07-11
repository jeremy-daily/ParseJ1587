#!/usr/env/python 
#-*- coding: utf-8 -*-
"""
Python Code
Created on Sat Jun 25 18:30:15 2016
by
author: jeremy-daily

Title: Parse J1587 Speed data

Description:

"""

import matplotlib.pyplot as plt

# import the data from the file into a list that is separated per line
fileName = "VSpy_log_of_network_traffic.csv"
with open(fileName) as logfile:
    logfiledata = logfile.readlines();
    
for logfileline in logfiledata:
    linedata = logfileline.split(',') # create lists based on the comma separator
    if len(linedata) > 7:    
        if linedata[7] == 'J1708':    
            print(linedata)
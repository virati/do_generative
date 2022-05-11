#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:57:02 2020

@author: virati
Delay Differential EQ Example
"""

from pylab import cos, linspace, subplots
from ddeint import ddeint


def model(Y, t):
    return -Y(t - 3 * cos(Y(t)) ** 2)


def values_before_zero(t):
    return 1


tt = linspace(0, 30, 2000)
yy = ddeint(model, values_before_zero, tt)

fig, ax = subplots(1, figsize=(4, 4))
ax.plot(tt, yy)
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 00:09:28 2017

@author: Paulina
"""


cur_x = 12 # The algorithm starts at x=6
gamma = 0.8 # step size multiplier
precision = 0.000001
previous_step_size = 2*precision

def f(x):
    return x**2-4*x+10

def df(x):
    return 2*x-4

i=1

while previous_step_size > precision:
    prev_x = cur_x
    cur_x += -gamma * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    i = i+1

print "Number of literations: ", i
print("The local minimum occurs at %f" % cur_x)
result= f(cur_x)
print "Value of the local minimum is:", result
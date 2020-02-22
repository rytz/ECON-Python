# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:12:49 2020

@author: rytz
"""

# Based on the example in Macroeconomics by Parkin, Section 2.2

import matplotlib.pyplot as plt

#============================================================

# Figure 1: PPF of Pizzas vs. Colas
fig1, ax1 = plt.subplots(num=1)

# define the points to plot
pizzas_prod =   [0,  1,  2,  3, 4, 5]
colas_prod =    [15, 14, 12, 9, 5, 0]

# define the x and y lists for the PPF
ppf_x = []
ppf_y = []
                 
# find the points on the PPF
for c in pizzas_prod :
    pt_x = pizzas_prod[c]
    pt_y = colas_prod[c]
    ppf_x.append(pt_x)
    ppf_y.append(pt_y)

# plot the PPF points
ax1.plot(ppf_x,ppf_y, 'bo')
    
# plot the PPF line using the values from each list
ax1.plot(pizzas_prod, colas_prod,c='b')    

## format the graph by editing boundaries and which values to use as ticks
# make the boundaries one more than each of the highest values
plt.xlim(0,pizzas_prod[-1]+1)
plt.ylim(0,colas_prod[0]+1)
# use only the values in the points as the ticks
plt.xticks(ppf_x)
plt.yticks(ppf_y)

# fill in the area below the PPF to contrast efficient vs. inefficient
ax1.fill_between(pizzas_prod, colas_prod, color='#539ecd')

# label the axes
plt.title('Production Possibilities Frontier: Pizzas vs. Colas')
plt.xlabel('Pizzas Produced')
plt.ylabel('Colas Produced')


#============================================================

# Figure 2: Allocative Efficiency (MB = MC)
fig2, ax2 = plt.subplots(num=2)

# define the x and y lists for the marginal cost (MC)
mc_x = []
mc_y = []

# calculate the points for the MC from the intervals between steps in ppf
for c in pizzas_prod :
    try :
        pt_x = (pizzas_prod[c]+pizzas_prod[c+1])/2
        pt_y = colas_prod[c]-colas_prod[c+1]
        mc_x.append(pt_x)
        mc_y.append(pt_y)
    except : 
        exit

# plot the points for the MC
ax2.plot(mc_x,mc_y,'r.')

# plot the line for the MC
ax2.plot(mc_x,mc_y)

# print the lists containing the MC points
#print("MC X values:",mc_x,'\nMC Y values: '+str(mc_y))

# define the points for the MB
mb_x =  [.5, 1.5, 2.5, 3.5, 4.5] # pizzas
mb_y =  [5,  4,   3,   2,   1] # colas per pizza

# format the graph with labels and a title
plt.title('Allocative Efficiency (MB = MC)')
plt.xlabel('Pizzas Produced')
plt.ylabel('Willingness to pay (colas per pizza)')

## format the graph by editing boundaries and which values to use as ticks
# make the boundaries one more than each of the highest values
plt.xlim(0,mc_x[-1]+1)
plt.ylim(0,mb_y[0]+1)
# use only the values in the points as the ticks
plt.xticks(mb_x+mc_x)
plt.yticks(mb_y+mc_y)

# plot the MB points
ax2.plot(mb_x,mb_y,'g.')

# plot the MB line
ax2.plot(mb_x,mb_y, c='m')

# get allocative efficiency point with nicely-aligning points in each line
for c in pizzas_prod :
    try:
        if mc_x[c] == mb_x[c] and mc_y[c] == mb_y[c] :
            allocative_efficiency = [mb_x,mb_y]
            plt.plot(mb_x[c],mc_y[c],'ok')
            print("Allocative Efficiency: " + str(mb_x[c]) + " colas per every " +  str(mb_y[c]) + " pizzas")
            exit
    except:
        exit

#============================================================

# find and print the intersection of the two lines using mathutils
import mathutils

lineA_p1 = mathutils.Vector((mc_x[0], mc_y[0]))
lineA_p2 = mathutils.Vector((mc_x[-1], mc_y[-1]))
lineB_p1 = mathutils.Vector((mb_x[0], mb_y[0]))
lineB_p2 = mathutils.Vector((mb_x[-1], mb_y[-1]))

allocative_efficiency = mathutils.geometry.intersect_line_line_2d(lineA_p1, lineA_p2, lineB_p1, lineB_p2)

print('mathutils intersection:',str(allocative_efficiency))








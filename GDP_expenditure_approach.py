# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 08:30:26 2020

@author: rytz
"""

def GDP_CIGXM_in_billions(consumption, investment, government, exports, imports) :
    
    # Consumption expenditures (C)
    C = consumption
    
    # Investment by firms // NEW capital per time period (I)
    I = investment
    
    # Goods and services bought by governments (G)
    G = government
    
    # Value of exports (X)
    X = exports
    
    # Value of imports (M)
    M = imports
    
    # Net exports (NX)
    NX = X - M
    
    # Aggregate Expenditures 
    E = C + I + G + NX
    
    # Gross Domestic Product (Aggregate Production)
    GDP = E
    
    # Percentage of GDP calculation
    C_percent = C / GDP * 100
    I_percent = I / GDP * 100
    G_percent = G / GDP * 100
    NX_percent = NX / GDP * 100
    
    # format the final GDP figure in dollars and with commas for readability
    import locale
    locale.setlocale(locale.LC_ALL, '')
    GDP_formatted = "$"+str(locale.format_string("%d", GDP*1000000000, grouping=True))


    # print the results
    print ("GDP        =",GDP_formatted)
    print ("C, of GDP  =",'{:.2f}'.format(round(C_percent,2),2)+"%")
    print ("I, of GDP  =",'{:.2f}'.format(round(I_percent,2),2)+"%")
    print ("G, of GDP  =",'{:.2f}'.format(round(G_percent,2),2)+"%")
    print ("NX, of GDP =",'{:.2f}'.format(round(NX_percent,2),2)+"%")
    


# call the function with your values (example from 2010Q2 data from US Commerce Dept)
GDP_CIGXM_in_billions(12758, 3036, 3277, 1000, 1502)




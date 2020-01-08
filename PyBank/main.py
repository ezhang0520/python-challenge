# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 19:08:29 2020

@author: elliezhang
"""

import pandas as pd
import numpy as np  

budget = pd.read_csv('budget_data.csv')
n = len(budget)

# compute total number of unique months
budget['Date_c'] = pd.to_datetime(budget['Date']).dt.date
budget.sort_values(by = ['Date_c'], inplace = True) 
budget['year'] = pd.DatetimeIndex(budget['Date_c']).year
budget['month'] = pd.DatetimeIndex(budget['Date_c']).month
n_m = (budget['year'][n-1] - budget['year'][0]) * 12 + (budget['month'][n-1] -  budget['month'][0]) + 1

# compute net amount of PnL
net_pnl = np.sum(budget['Profit/Losses'] )

# compute average change
budget['pnl_change'] = budget['Profit/Losses'] - budget['Profit/Losses'].shift(1)
avg_change = round(np.mean(budget['pnl_change'] ), 2)

# compute greatest increase
g_i = np.max(budget['pnl_change'])
date_i = budget.loc[budget['pnl_change'].idxmax(), 'Date']

# compute greatest decrease
g_d = np.min(budget['pnl_change'])
date_d = budget.loc[budget['pnl_change'].idxmin(), 'Date']

# print results
print('Financial Analysis')
print('---------------------')
print('Total Months: ' + str(n_m))
print('Total: $' + str(net_pnl))
print('Average Change: $' + str(avg_change))
print ("Greatest Increase in Proftis: %s ($%i)" % (date_i, int(g_i)))
print ("Greatest Decrease in Proftis: %s ($%i)" % (date_d, int(g_d)))

# write result file
with open('buget.txt', 'w') as f:
    f.write('Financial Analysis\n')
    f.write('---------------------\n')
    f.write('Total Months: ' + str(n_m) + '\n')
    f.write('Total: $' + str(net_pnl) + '\n')
    f.write('Average Change: $' + str(avg_change) + '\n')
    f.write ("Greatest Increase in Proftis: %s ($%i)" % (date_i, int(g_i)) + '\n')
    f.write ("Greatest Decrease in Proftis: %s ($%i)" % (date_d, int(g_d)))
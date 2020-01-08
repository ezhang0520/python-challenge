# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 19:47:45 2020

@author: elliezhang
"""

import pandas as pd

election = pd.read_csv('election_data.csv')

# compute total number of votes
n = len(election)

# get a list of candidates
can_ls = list(set(election['Candidate'].values))

# compute percentage of votes for each candidate
by_can = election.groupby('Candidate').size()
can_dict = dict(zip(by_can.index, by_can.values))

# get_winner
winner = max(can_dict, key = can_dict.get)

# print results
print('Election Results')
print('------------------')
print('Total Votes: ' + str(n))
print('------------------')
for key, val in can_dict.items():
    per = round(val/n*100, 3)
    print('%s: %.3f%%(%i)' % (key, per, val))
print('------------------')
print('Winner: ' + winner)

# write result file
with open('election.txt', 'w') as f:
    f.write('Election Results\n')
    f.write('------------------\n')
    f.write('Total Votes: ' + str(n) +'\n')
    f.write('------------------\n')
    for key, val in can_dict.items():
        per = round(val/n*100, 3)
        f.write('%s: %.3f%%(%i)\n' % (key, per, val))
    f.write('------------------\n')
    f.write('Winner: ' + winner)


    
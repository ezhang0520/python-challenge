#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:58:32 2020

@author: elliezhang
"""


import numpy as np

# define a function to conduct paragraph analysis
def para_analysis(para, out_file_name):
    para_contents = para.read()
    
    # split paragraphs to words
    words_all = para_contents.split()
    
    # split paragraphs to sentences
    sentence_all = para_contents.split('.')[:-1]
    
    # get the length of each word
    words_len = [len(i) for i  in words_all]
    
    # get the length of each sentence
    sen_len = [len(i.split()) for i in sentence_all]
    
    # calculate and print results
    print('Paragraph Analysis')
    print('------------------')
    print('Approximate Word Count: ', len(words_all))
    print('Approximate Sentence Count: ', len(sentence_all))
    print('Average letter Count: ', round(np.mean(words_len),1))
    print('Average Sentence Length: ', round(np.mean(sen_len),1))
     
    # write result file
    
    with open(out_file_name +'.txt', 'w') as f:
        f.write('Paragraph Analysis\n')
        f.write('------------------\n')
        f.write('Approximate Word Count: '+ str(len(words_all)) + '\n')
        f.write('Approximate Sentence Count: ' + str(len(sentence_all)) + '\n')
        f.write('Average letter Count: '+ str(round(np.mean(words_len),1)) + '\n')
        f.write('Average Sentence Length: ' + str(round(np.mean(sen_len),1)) + '\n')

with open('paragraph_1.txt', 'r') as para1:
    para_analysis(para1, 'paragraph_1_analysis')

with open('paragraph_2.txt', 'r') as para2:
    para_analysis(para2, 'paragraph_2_analysis')

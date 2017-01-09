# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:45:22 2016

@author: wang
"""
#from matplotlib import pylab as plt
#from numpy import fft, fromstring, int16, linspace
#import wave

from read_wav_xml_good_1 import*
from matrix_24_2 import*
from max_matrix_norm import*

import numpy as np
# open a wave file
filename = 'francois_filon_pure_2.wav'
filename_1 ='francois_filon_pure_2.xml'
word ='je'

wave_signal_float,framerate, word_start_point, word_length_point, word_end_point= read_wav_xml_good_1(filename,filename_1,word)
print 'word_start_point=',word_start_point
print 'word_length_point=',word_length_point
print 'word_end_point=',word_end_point




XJ_1 =wave_signal_float

t_step=1920;
t_entre_step=1440;

t_du_1_1 = int(word_start_point[0]);
t_du_1_2 = int(word_end_point[0]);

t_du_2_1 = int(word_start_point[1]);
t_du_2_2 = int(word_end_point[1]);

t_du_3_1 = int(word_start_point[2]);
t_du_3_2 = int(word_end_point[2]);

#t_du_4_1 = int(word_start_point[3]);
#t_du_4_2 = int(word_end_point[3]);
#
#t_du_5_1 = int(word_start_point[4]);
#t_du_5_2 = int(word_end_point[4]);
fs=framerate
#XJ_du_1 = wave_signal_float[(t_du_1_1-1):t_du_1_2];
#length_XJ_du_1 = int(word_length_point[0]+1);
#x1,y1,z1=matrix_24_2(XJ_du_1,fs)
#x1=max_matrix_norm(x1)


#==============================================================================
# this part is to calcul the first matrix 
#==============================================================================
XJ_du_1_2 = XJ_1[(t_du_1_1-1):(t_du_1_1+t_step)];
x1_1,y1_1,z1_1=matrix_24_2(XJ_du_1_2 ,fs)
x1_1=max_matrix_norm(x1_1)
matrix_all_step_new_1 = np.zeros([192])

for i in range(0,24):
    matrix_all_step_new_1[i]=x1_1[i]
#==============================================================================
# the other colonne is the all fft
#==============================================================================
for i in range(1,8):
    XJ_du_1_total = XJ_1[(t_du_1_1+t_entre_step*(i)-1):(t_du_1_1+t_step+t_entre_step*(i) )];
    x1_all,y1_all,z1_all=matrix_24_2(XJ_du_1_total,fs)
    x1_all=max_matrix_norm(x1_all)
    for j in range(0,24):
        matrix_all_step_new_1[24*i+j]=x1_all[j]

#==============================================================================
# this part is to calcul the second matrix
#==============================================================================
for k in range (1,2):
    t_start=t_du_2_1
    XJ_du_1_2 = XJ_1[(t_start-1):(t_start+t_step)];
    x1_1,y1_1,z1_1=matrix_24_2(XJ_du_1_2 ,fs)
    x1_1=max_matrix_norm(x1_1)
    matrix_all_step_new_2 = np.zeros([192])
    for i in range(0,24):
        matrix_all_step_new_2[i]=x1_1[i]
#==============================================================================
# the other colonne is the all fft
#==============================================================================
    for i in range(1,8):
        XJ_du_1_total = XJ_1[(t_start+t_entre_step*(i)-1):(t_start+t_step+t_entre_step*(i) )];
        x1_all,y1_all,z1_all=matrix_24_2(XJ_du_1_total,fs)
        x1_all=max_matrix_norm(x1_all)
        for j in range(0,24):
            matrix_all_step_new_2[24*i+j]=x1_all[j]
            
#==============================================================================
# this part is to calcul the 3 matrix
#==============================================================================
for k in range (1,2):
    t_start=t_du_3_1
    XJ_du_1_2 = XJ_1[(t_start-1):(t_start+t_step)];
    x1_1,y1_1,z1_1=matrix_24_2(XJ_du_1_2 ,fs)
    x1_1=max_matrix_norm(x1_1)
    matrix_all_step_new_3 = np.zeros([192])
    for i in range(0,24):
        matrix_all_step_new_3[i]=x1_1[i]
#==============================================================================
# the other colonne is the all fft
#==============================================================================
    for i in range(1,8):
        XJ_du_1_total = XJ_1[(t_start+t_entre_step*(i)-1):(t_start+t_step+t_entre_step*(i) )];
        x1_all,y1_all,z1_all=matrix_24_2(XJ_du_1_total,fs)
        x1_all=max_matrix_norm(x1_all)
        for j in range(0,24):  
            matrix_all_step_new_3[24*i+j]=x1_all[j]
#
##==============================================================================
## this part is to calcul the 4 matrix
##==============================================================================
#for k in range (1,2):
#    t_start=t_du_4_1
#    XJ_du_1_2 = XJ_1[(t_start-1):(t_start+t_step)];
#    x1_1,y1_1,z1_1=matrix_24_2(XJ_du_1_2 ,fs)
#    x1_1=max_matrix_norm(x1_1)
#    matrix_all_step_new_4 = np.zeros([192])
#    for i in range(0,24):
#        matrix_all_step_new_4[i]=x1_1[i]
##==============================================================================
## the other colonne is the all fft
##==============================================================================
#    for i in range(1,8):
##        print i
#        XJ_du_1_total = XJ_1[(t_start+t_entre_step*(i)-1):(t_start+t_step+t_entre_step*(i) )];
#        x1_all,y1_all,z1_all=matrix_24_2(XJ_du_1_total,fs)
#        x1_all=max_matrix_norm(x1_all)
#        for j in range(0,24):
#            matrix_all_step_new_4[24*i+j]=x1_all[j]
##print 'matrix_all_step_4=',matrix_all_step_4

##==============================================================================
## this part is to calcul the 5 matrix
##==============================================================================
#for k in range (1,2):
#    t_start=t_du_5_1
#    XJ_du_1_2 = XJ_1[(t_start-1):(t_start+t_step)];
#    x1_1,y1_1,z1_1=matrix_24_2(XJ_du_1_2 ,fs)
#    x1_1=max_matrix_norm(x1_1)
#    matrix_all_step_new_5 = np.zeros([192])
#    for i in range(0,24):
#        matrix_all_step_new_5[i]=x1_1[i]
##==============================================================================
## the other colonne is the all fft
##==============================================================================
#    for i in range(1,8):
##        print i
#        XJ_du_1_total = XJ_1[(t_start+t_entre_step*(i)-1):(t_start+t_step+t_entre_step*(i) )];
#        x1_all,y1_all,z1_all=matrix_24_2(XJ_du_1_total,fs)
#        x1_all=max_matrix_norm(x1_all)
#        for j in range(0,24):
#            matrix_all_step_new_5[24*i+j]=x1_all[j]  
##print 'matrix_all_step_5=',matrix_all_step_5

#np.savez('je_compare_192_matrix_2.npz',matrix_all_step_new_1,matrix_all_step_new_2,matrix_all_step_new_3,matrix_all_step_new_4,matrix_all_step_new_5)

np.savez('je_compare_192_matrix_3_je.npz',matrix_all_step_new_1,matrix_all_step_new_2,matrix_all_step_new_3)

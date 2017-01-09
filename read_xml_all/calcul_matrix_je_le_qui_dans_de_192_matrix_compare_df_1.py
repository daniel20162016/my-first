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
#filename = 'francois_filon_pure_3.wav'
#filename_1 ='francois_filon_pure_3.xml'
#word ='je'
#word_2='le'
#word_3='qui'
#word_4='dans'
#word_5='de'


def calcul_matrix_je_le_qui_dans_de_192_matrix_compare_df_1(filename, filename_1,word,word_2,word_3,word_4,word_5):
#==============================================================================
# this is the parti for the 'je'  start
#==============================================================================
    wave_signal_float,framerate, word_start_point, word_length_point, word_end_point= read_wav_xml_good_1(filename,filename_1,word)
    XJ_1 =wave_signal_float
    t_step=1920;
    t_entre_step=1440;
    t_du_1_1 = int(word_start_point[0]);
    t_du_1_2 = int(word_end_point[0]);
    t_du_2_1 = int(word_start_point[1]);
    t_du_2_2 = int(word_end_point[1]);
    t_du_3_1 = int(word_start_point[2]);
    t_du_3_2 = int(word_end_point[2]);
    t_du_4_1 = int(word_start_point[3]);
    t_du_4_2 = int(word_end_point[3]);
    t_du_5_1 = int(word_start_point[4]);
    t_du_5_2 = int(word_end_point[4]);
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
#==============================================================================
# this part is to calcul the 4 matrix
#==============================================================================
    for k in range (1,2):
        t_start=t_du_4_1
        XJ_du_1_2 = XJ_1[(t_start-1):(t_start+t_step)];
        x1_1,y1_1,z1_1=matrix_24_2(XJ_du_1_2 ,fs)
        x1_1=max_matrix_norm(x1_1)
        matrix_all_step_new_4 = np.zeros([192])
        for i in range(0,24):
            matrix_all_step_new_4[i]=x1_1[i]
#==============================================================================
# the other colonne is the all fft
#==============================================================================
        for i in range(1,8):
#        print i
            XJ_du_1_total = XJ_1[(t_start+t_entre_step*(i)-1):(t_start+t_step+t_entre_step*(i) )];
            x1_all,y1_all,z1_all=matrix_24_2(XJ_du_1_total,fs)
            x1_all=max_matrix_norm(x1_all)
            for j in range(0,24):
                matrix_all_step_new_4[24*i+j]=x1_all[j]
#==============================================================================
# this part is to calcul the 5 matrix
#==============================================================================
    for k in range (1,2):
        t_start=t_du_5_1
        XJ_du_1_2 = XJ_1[(t_start-1):(t_start+t_step)];
        x1_1,y1_1,z1_1=matrix_24_2(XJ_du_1_2 ,fs)
        x1_1=max_matrix_norm(x1_1)
        matrix_all_step_new_5 = np.zeros([192])
        for i in range(0,24):
            matrix_all_step_new_5[i]=x1_1[i]
#==============================================================================
# the other colonne is the all fft
#==============================================================================
        for i in range(1,8):
#        print i
            XJ_du_1_total = XJ_1[(t_start+t_entre_step*(i)-1):(t_start+t_step+t_entre_step*(i) )];
            x1_all,y1_all,z1_all=matrix_24_2(XJ_du_1_total,fs)
            x1_all=max_matrix_norm(x1_all)
            for j in range(0,24):
                matrix_all_step_new_5[24*i+j]=x1_all[j] 
    je_compare_1 = matrix_all_step_new_1
    je_compare_2 = matrix_all_step_new_2
    je_compare_3 = matrix_all_step_new_3
    je_compare_4 = matrix_all_step_new_4
    je_compare_5 = matrix_all_step_new_5 
#==============================================================================
#       # this is the parti for the 'je'  end       
#==============================================================================          
#np.savez('je_le_qui_dans_de_192_matrix.npz',matrix_all_step_new_1,matrix_all_step_new_2,matrix_all_step_new_3,matrix_all_step_new_4,matrix_all_step_new_5)


#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
# # # # # # # #  demain, je continue ici
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================

#==============================================================================
# this is the parti for the 'le'  start
#==============================================================================
    wave_signal_float,framerate, word_start_point, word_length_point, word_end_point= read_wav_xml_good_1(filename,filename_1,word_2)
    XJ_1 =wave_signal_float
    t_step=1920;
    t_entre_step=1440;
    t_du_1_1 = int(word_start_point[0]);
    t_du_1_2 = int(word_end_point[0]);
    t_du_2_1 = int(word_start_point[1]);
    t_du_2_2 = int(word_end_point[1]);
    t_du_3_1 = int(word_start_point[2]);
    t_du_3_2 = int(word_end_point[2]);
    t_du_4_1 = int(word_start_point[3]);
    t_du_4_2 = int(word_end_point[3]);
    t_du_5_1 = int(word_start_point[4]);
    t_du_5_2 = int(word_end_point[4]);
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
#==============================================================================
# this part is to calcul the 4 matrix
#==============================================================================
    for k in range (1,2):
        t_start=t_du_4_1
        XJ_du_1_2 = XJ_1[(t_start-1):(t_start+t_step)];
        x1_1,y1_1,z1_1=matrix_24_2(XJ_du_1_2 ,fs)
        x1_1=max_matrix_norm(x1_1)
        matrix_all_step_new_4 = np.zeros([192])
        for i in range(0,24):
            matrix_all_step_new_4[i]=x1_1[i]
#==============================================================================
# the other colonne is the all fft
#==============================================================================
        for i in range(1,8):
#        print i
            XJ_du_1_total = XJ_1[(t_start+t_entre_step*(i)-1):(t_start+t_step+t_entre_step*(i) )];
            x1_all,y1_all,z1_all=matrix_24_2(XJ_du_1_total,fs)
            x1_all=max_matrix_norm(x1_all)
            for j in range(0,24):
                matrix_all_step_new_4[24*i+j]=x1_all[j]
#==============================================================================
# this part is to calcul the 5 matrix
#==============================================================================
    for k in range (1,2):
        t_start=t_du_5_1
        XJ_du_1_2 = XJ_1[(t_start-1):(t_start+t_step)];
        x1_1,y1_1,z1_1=matrix_24_2(XJ_du_1_2 ,fs)
        x1_1=max_matrix_norm(x1_1)
        matrix_all_step_new_5 = np.zeros([192])
        for i in range(0,24):
            matrix_all_step_new_5[i]=x1_1[i]
#==============================================================================
# the other colonne is the all fft
#==============================================================================
        for i in range(1,8):
#        print i
            XJ_du_1_total = XJ_1[(t_start+t_entre_step*(i)-1):(t_start+t_step+t_entre_step*(i) )];
            x1_all,y1_all,z1_all=matrix_24_2(XJ_du_1_total,fs)
            x1_all=max_matrix_norm(x1_all)
            for j in range(0,24):
                matrix_all_step_new_5[24*i+j]=x1_all[j] 
    le_compare_1 = matrix_all_step_new_1
    le_compare_2 = matrix_all_step_new_2
    le_compare_3 = matrix_all_step_new_3
    le_compare_4 = matrix_all_step_new_4
    le_compare_5 = matrix_all_step_new_5 

#==============================================================================
#       # this is the parti for the 'le'  end       
#==============================================================================      



#==============================================================================
# this is the parti for the 'qui'  start
#==============================================================================
    wave_signal_float,framerate, word_start_point, word_length_point, word_end_point= read_wav_xml_good_1(filename,filename_1,word_3)
    XJ_1 =wave_signal_float
    t_step=1920;
    t_entre_step=1440;
    t_du_1_1 = int(word_start_point[0]);
    t_du_1_2 = int(word_end_point[0]);
    t_du_2_1 = int(word_start_point[1]);
    t_du_2_2 = int(word_end_point[1]);
    t_du_3_1 = int(word_start_point[2]);
    t_du_3_2 = int(word_end_point[2]);
    t_du_4_1 = int(word_start_point[3]);
    t_du_4_2 = int(word_end_point[3]);
    t_du_5_1 = int(word_start_point[4]);
    t_du_5_2 = int(word_end_point[4]);
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
#==============================================================================
# this part is to calcul the 4 matrix
#==============================================================================
    for k in range (1,2):
        t_start=t_du_4_1
        XJ_du_1_2 = XJ_1[(t_start-1):(t_start+t_step)];
        x1_1,y1_1,z1_1=matrix_24_2(XJ_du_1_2 ,fs)
        x1_1=max_matrix_norm(x1_1)
        matrix_all_step_new_4 = np.zeros([192])
        for i in range(0,24):
            matrix_all_step_new_4[i]=x1_1[i]
#==============================================================================
# the other colonne is the all fft
#==============================================================================
        for i in range(1,8):
#        print i
            XJ_du_1_total = XJ_1[(t_start+t_entre_step*(i)-1):(t_start+t_step+t_entre_step*(i) )];
            x1_all,y1_all,z1_all=matrix_24_2(XJ_du_1_total,fs)
            x1_all=max_matrix_norm(x1_all)
            for j in range(0,24):
                matrix_all_step_new_4[24*i+j]=x1_all[j]
#==============================================================================
# this part is to calcul the 5 matrix
#==============================================================================
    for k in range (1,2):
        t_start=t_du_5_1
        XJ_du_1_2 = XJ_1[(t_start-1):(t_start+t_step)];
        x1_1,y1_1,z1_1=matrix_24_2(XJ_du_1_2 ,fs)
        x1_1=max_matrix_norm(x1_1)
        matrix_all_step_new_5 = np.zeros([192])
        for i in range(0,24):
            matrix_all_step_new_5[i]=x1_1[i]
#==============================================================================
# the other colonne is the all fft
#==============================================================================
        for i in range(1,8):
#        print i
            XJ_du_1_total = XJ_1[(t_start+t_entre_step*(i)-1):(t_start+t_step+t_entre_step*(i) )];
            x1_all,y1_all,z1_all=matrix_24_2(XJ_du_1_total,fs)
            x1_all=max_matrix_norm(x1_all)
            for j in range(0,24):
                matrix_all_step_new_5[24*i+j]=x1_all[j] 
    qui_compare_1 = matrix_all_step_new_1
    qui_compare_2 = matrix_all_step_new_2
    qui_compare_3 = matrix_all_step_new_3
    qui_compare_4 = matrix_all_step_new_4
    qui_compare_5 = matrix_all_step_new_5 


#==============================================================================
# this is the parti for the 'dans'  start
#==============================================================================
    wave_signal_float,framerate, word_start_point, word_length_point, word_end_point= read_wav_xml_good_1(filename,filename_1,word_4)
    XJ_1 =wave_signal_float
    t_step=1920;
    t_entre_step=1440;
    t_du_1_1 = int(word_start_point[0]);
    t_du_1_2 = int(word_end_point[0]);
    t_du_2_1 = int(word_start_point[1]);
    t_du_2_2 = int(word_end_point[1]);
    t_du_3_1 = int(word_start_point[2]);
    t_du_3_2 = int(word_end_point[2]);
    t_du_4_1 = int(word_start_point[3]);
    t_du_4_2 = int(word_end_point[3]);
    t_du_5_1 = int(word_start_point[4]);
    t_du_5_2 = int(word_end_point[4]);
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
#==============================================================================
# this part is to calcul the 4 matrix
#==============================================================================
    for k in range (1,2):
        t_start=t_du_4_1
        XJ_du_1_2 = XJ_1[(t_start-1):(t_start+t_step)];
        x1_1,y1_1,z1_1=matrix_24_2(XJ_du_1_2 ,fs)
        x1_1=max_matrix_norm(x1_1)
        matrix_all_step_new_4 = np.zeros([192])
        for i in range(0,24):
            matrix_all_step_new_4[i]=x1_1[i]
#==============================================================================
# the other colonne is the all fft
#==============================================================================
        for i in range(1,8):
#        print i
            XJ_du_1_total = XJ_1[(t_start+t_entre_step*(i)-1):(t_start+t_step+t_entre_step*(i) )];
            x1_all,y1_all,z1_all=matrix_24_2(XJ_du_1_total,fs)
            x1_all=max_matrix_norm(x1_all)
            for j in range(0,24):
                matrix_all_step_new_4[24*i+j]=x1_all[j]
#==============================================================================
# this part is to calcul the 5 matrix
#==============================================================================
    for k in range (1,2):
        t_start=t_du_5_1
        XJ_du_1_2 = XJ_1[(t_start-1):(t_start+t_step)];
        x1_1,y1_1,z1_1=matrix_24_2(XJ_du_1_2 ,fs)
        x1_1=max_matrix_norm(x1_1)
        matrix_all_step_new_5 = np.zeros([192])
        for i in range(0,24):
            matrix_all_step_new_5[i]=x1_1[i]
#==============================================================================
# the other colonne is the all fft
#==============================================================================
        for i in range(1,8):
#        print i
            XJ_du_1_total = XJ_1[(t_start+t_entre_step*(i)-1):(t_start+t_step+t_entre_step*(i) )];
            x1_all,y1_all,z1_all=matrix_24_2(XJ_du_1_total,fs)
            x1_all=max_matrix_norm(x1_all)
            for j in range(0,24):
                matrix_all_step_new_5[24*i+j]=x1_all[j] 
    dans_compare_1 = matrix_all_step_new_1
    dans_compare_2 = matrix_all_step_new_2
    dans_compare_3 = matrix_all_step_new_3
    dans_compare_4 = matrix_all_step_new_4
    dans_compare_5 = matrix_all_step_new_5


#==============================================================================
# this is the parti for the 'de'  start
#==============================================================================
    wave_signal_float,framerate, word_start_point, word_length_point, word_end_point= read_wav_xml_good_1(filename,filename_1,word_5)
    XJ_1 =wave_signal_float
    t_step=1920;
    t_entre_step=1440;
    t_du_1_1 = int(word_start_point[0]);
    t_du_1_2 = int(word_end_point[0]);
    t_du_2_1 = int(word_start_point[1]);
    t_du_2_2 = int(word_end_point[1]);
    t_du_3_1 = int(word_start_point[2]);
    t_du_3_2 = int(word_end_point[2]);
    t_du_4_1 = int(word_start_point[3]);
    t_du_4_2 = int(word_end_point[3]);
    t_du_5_1 = int(word_start_point[4]);
    t_du_5_2 = int(word_end_point[4]);
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
#==============================================================================
# this part is to calcul the 4 matrix
#==============================================================================
    for k in range (1,2):
        t_start=t_du_4_1
        XJ_du_1_2 = XJ_1[(t_start-1):(t_start+t_step)];
        x1_1,y1_1,z1_1=matrix_24_2(XJ_du_1_2 ,fs)
        x1_1=max_matrix_norm(x1_1)
        matrix_all_step_new_4 = np.zeros([192])
        for i in range(0,24):
            matrix_all_step_new_4[i]=x1_1[i]
#==============================================================================
# the other colonne is the all fft
#==============================================================================
        for i in range(1,8):
#        print i
            XJ_du_1_total = XJ_1[(t_start+t_entre_step*(i)-1):(t_start+t_step+t_entre_step*(i) )];
            x1_all,y1_all,z1_all=matrix_24_2(XJ_du_1_total,fs)
            x1_all=max_matrix_norm(x1_all)
            for j in range(0,24):
                matrix_all_step_new_4[24*i+j]=x1_all[j]
#==============================================================================
# this part is to calcul the 5 matrix
#==============================================================================
    for k in range (1,2):
        t_start=t_du_5_1
        XJ_du_1_2 = XJ_1[(t_start-1):(t_start+t_step)];
        x1_1,y1_1,z1_1=matrix_24_2(XJ_du_1_2 ,fs)
        x1_1=max_matrix_norm(x1_1)
        matrix_all_step_new_5 = np.zeros([192])
        for i in range(0,24):
            matrix_all_step_new_5[i]=x1_1[i]
#==============================================================================
# the other colonne is the all fft
#==============================================================================
        for i in range(1,8):
#        print i
            XJ_du_1_total = XJ_1[(t_start+t_entre_step*(i)-1):(t_start+t_step+t_entre_step*(i) )];
            x1_all,y1_all,z1_all=matrix_24_2(XJ_du_1_total,fs)
            x1_all=max_matrix_norm(x1_all)
            for j in range(0,24):
                matrix_all_step_new_5[24*i+j]=x1_all[j] 
    de_compare_1 = matrix_all_step_new_1
    de_compare_2 = matrix_all_step_new_2
    de_compare_3 = matrix_all_step_new_3
    de_compare_4 = matrix_all_step_new_4
    de_compare_5 = matrix_all_step_new_5 

#==============================================================================
#       # this is the parti for the 'le'  end       
#==============================================================================    
    np.savez('je_le_qui_dans_de_192_matrix_compare.npz',je_compare_1,je_compare_2,je_compare_3,je_compare_4,je_compare_5,le_compare_1,le_compare_2,le_compare_3,le_compare_4,le_compare_5,qui_compare_1,qui_compare_2,qui_compare_3,qui_compare_4,qui_compare_5,dans_compare_1,dans_compare_2,dans_compare_3,dans_compare_4,dans_compare_5,de_compare_1,de_compare_2,de_compare_3,de_compare_4,de_compare_5)
    finish_2=1
    return finish_2
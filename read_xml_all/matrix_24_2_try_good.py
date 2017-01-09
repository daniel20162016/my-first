# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:45:22 2016

@author: wang
"""
#from matplotlib import pylab as plt
from numpy import fft, fromstring, int16, linspace
import numpy as np
#from scipy.fftpack import fft, ifft
#import wave

from matplotlib import pylab as plt
import math

from read_wav_xml_good_1 import*

# open a wave file
filename = 'francois_filon_pure_1.wav'
filename_1 ='francois_filon_pure_1.xml'
word ='je'

wave_signal_float,framerate, word_start_point, word_length_point, word_end_point= read_wav_xml_good_1(filename,filename_1,word)
print 'word_start_point=',word_start_point
print 'word_length_point=',word_length_point
print 'word_end_point=',word_end_point
fs=framerate;

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


XJ_du_1 = wave_signal_float[(t_du_1_1-1):t_du_1_2];
yy_1=XJ_du_1;
length_XJ_du_1 = int(word_length_point[0]+1);

matrix_24=np.zeros(24);
#print matrix_24

length_yy_1=length_XJ_du_1;
N=length_yy_1;
print 'n=',N;

fs_float=float(fs);
N_float=float(N);
fs_N=(N_float-1)/fs_float;
t=np.linspace(0,fs_N,N)

#print len(yy_1)
#fft_y_1=fft(yy_1,N)

#x=np.array([1.0,2.0,1.0,-1.0,1.5])
#y=fft(x)
#
xtimes      = linspace(0,N,N)
#
#plt.plot(xtimes, yy_1)
#plt.grid()
#plt.show()

y=np.fft.fft(yy_1)
#print ('yy_1=',yy_1[0])

mag_fft_y_1=abs(y);
f_fft_y_1=np.linspace(0,fs_float, N)  #f_fft_y_1 = n*fs/N

step_50 = int(50/f_fft_y_1[1])
step_250 = int(250/f_fft_y_1[1])

matrix_24[0]=sum(mag_fft_y_1[0:step_50+1])
print 'matrix_24[0]=',matrix_24[0]

for i in range(1,20):
     matrix_24[i]= sum(mag_fft_y_1[(1+step_50*i):(step_50*(i+1))])
     print 'matrix_24_',i,'=',matrix_24[i]

for i in range(20,24):
    matrix_24[i]= sum(mag_fft_y_1[(1+step_250*i):(step_250*(i+1))])
    print 'matrix_24_',i,'=',matrix_24[i]
#    
#print matrix_24

#print 'step_250=',step_250

#print f_fft_y_1[8160]

#print (mag_fft_y_1)
#
#plt.plot(xtimes, mag_fft_y_1)
#plt.grid()
#plt.show()

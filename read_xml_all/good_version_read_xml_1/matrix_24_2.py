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



def matrix_24_2(yy_1,fs):
    matrix_24=np.zeros(24);
    length_yy_1=len(yy_1);
    N=length_yy_1;
    fs_float=float(fs);
    N_float=float(N);
    fs_N=(N_float-1)/fs_float;
#plt.plot(xtimes, yy_1)
#plt.grid()
#plt.show()
    y=np.fft.fft(yy_1)
    mag_fft_y_1=abs(y);
    f_fft_y_1=np.linspace(0,fs_float, N)  #f_fft_y_1 = n*fs/N
    step_50 = int(50/f_fft_y_1[1])
    step_250 = int(250/f_fft_y_1[1])
    matrix_24[0]=sum(mag_fft_y_1[0:step_50+1])
#    print 'matrix_24[0]=',matrix_24[0]
    for i in range(1,20):
        matrix_24[i]= sum(mag_fft_y_1[(1+step_50*i):(step_50*(i+1))])
#        print 'matrix_24_',i,'=',matrix_24[i]
    for i in range(20,24):
        matrix_24[i]= sum(mag_fft_y_1[(1+step_250*i):(step_250*(i+1))])
#        print 'matrix_24_',i,'=',matrix_24[i]
    return matrix_24,f_fft_y_1,mag_fft_y_1


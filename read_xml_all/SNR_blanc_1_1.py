# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:15:50 2016

@author: wang
"""
#from matplotlib import pylab as plt
#from numpy import fft, fromstring, int16, linspace
#import wave
#import numpy as np
#from scipy import signal
#import pylab as pl
#import shutil
import wave
#from os import system
#import json
#from choc_reduce_main_2 import*
import sys
#from os import path
#from matplotlib import pylab as plt
from numpy import fft, fromstring, int16, linspace, zeros
from math import log10

filename = sys.argv[1]
#filename = 'out_01.wav'
mode     = 'rb'   # mode can be : 'r' (for read), 'w' (write), 'rb' (read like a binary file) or 'wb' (write like a binary file)
file_read = wave.open(filename,mode)
params = file_read.getparams() # This variable return several values ( nchannels, sampwith, framerate, nframe, comptype, compname)
nchannels = params[0]   # the number of channel (1 for mono / 2 for stereo)
sampwith  = params[1]   # in octet (number of bit coding)
framerate = params[2]   # the samples rate (in Hz)
nframes   = params[3]   # number of samples
wave_signal_string = file_read.readframes(nframes)   # get the samples contening in the wave file (in string format)
wave_signal_int16 = fromstring(wave_signal_string,int16)
wave_signal_float = 1* wave_signal_int16.astype(float)
Nsamples    = len(wave_signal_float)
xtimes      = linspace(0,Nsamples,Nsamples)
abs_wave_signal_float=abs(wave_signal_float)
#plt.plot(xtimes,abs_wave_signal_float)
#plt.grid()
#plt.show()
#### filter the signal,,, begin
length_wave_signal_float= len(wave_signal_float)
s=wave_signal_float
t_total=length_wave_signal_float/framerate
file_read.close()
delta_t = 0.0125
t_win =int( delta_t*framerate)
t_number_win = int( length_wave_signal_float/t_win)
power_win = zeros(t_number_win)
len_power_win =len(power_win)
x_temp=abs_wave_signal_float[0:(t_win-1)]
power_win[0] =sum([ i*i for i in x_temp])
for j in range(1,t_number_win):
    a=0
    x_temp_2=abs_wave_signal_float[j*100:(j*100+100)]
    power_win[j]=sum([ i*i for i in x_temp_2])   
x_step=range(len_power_win)
#plt.plot(x_step,power_win)
#plt.grid()
#plt.show()
limit_min = max(power_win)/100
number_signal=0
number_bruit=0
power_limit=2
power_limit_amplitude=0
signal_total=zeros(len_power_win)
bruit_ = zeros(len_power_win)
for k in range(1,len_power_win):
    if power_win[k]>limit_min and (power_win[k]/power_win[k-1])>=power_limit:
        power_limit_amplitude = power_win[k]
        break   
for kk in range(1,len_power_win):
    if power_win[kk]>=power_limit_amplitude:
        signal_total[kk] = power_win[kk]
        number_signal=number_signal+1
    else:
        bruit_[kk]=power_win[kk]
        number_bruit=number_bruit+1        
#print number_signal
#print number_bruit 
power_signal_number_total = sum(signal_total)   
power_bruit_number_total = sum(bruit_)
average_bruit = power_bruit_number_total/number_bruit
bruit_total_numberofsignal = average_bruit*number_signal
#######
### the basic idea is to calcult the number of signal,, then, caulcul the bruit total in these number of signal (bruit_total_numberofsignal)
### then, use the power_signal_number_total - bruit_total_numberofsignal =pure_signal
#######
signal_pure_numberofsignal = power_signal_number_total - bruit_total_numberofsignal
#print signal_pure_numberofsignal
SNR_abs = signal_pure_numberofsignal/bruit_total_numberofsignal
print "Signal to noise ratio (absolute)"
print int(SNR_abs) 
SNR_db = 10*log10(SNR_abs)
print "Signal to noise ratio (db)"
print int(SNR_db)
   
   
   
   
  
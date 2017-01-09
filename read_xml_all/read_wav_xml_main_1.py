# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:45:22 2016

@author: wang
"""
#from matplotlib import pylab as plt
#from numpy import fft, fromstring, int16, linspace
#import wave
from read_wav_xml_good_1 import*

# open a wave file
filename = 'francois_filon_pure_1.wav'
filename_1 ='francois_filon_pure_1.xml'
word ='je'


wave_signal_float,framerate, word_start_point, word_end_point= read_wav_xml_good_1(filename,filename_1,word)
print 'word_start_point=',word_start_point

print 'word_end_point=',word_end_point
#
#def read_wav_xml_good_1(filename, filename_1,word):
#    mode     = 'rb'   # mode can be : 'r' (for read), 'w' (write), 'rb' (read like a binary file) or 'wb' (write like a binary file)
#    file_read = wave.open(filename,mode)
## to get the wave file parameters
#    params = file_read.getparams() # This variable return several values ( nchannels, sampwith, framerate, nframe, comptype, compname)
#    nchannels = params[0]   # the number of channel (1 for mono / 2 for stereo)
#    sampwith  = params[1]   # in octet (number of bit coding)
#    framerate = params[2]   # the samples rate (in Hz)
#    nframes   = params[3]   # number of samples
## to get the waveforme of the wave file
#    wave_signal_string = file_read.readframes(nframes)   # get the samples contening in the wave file (in string format)
## conversion to int16 in into float
#    wave_signal_int16 = fromstring(wave_signal_string,int16)
#    wave_signal_float = 1* wave_signal_int16.astype(float)
## plotting 
#    Nsamples    = len(wave_signal_float)
#    xtimes      = linspace(0,Nsamples,Nsamples)
##plt.plot(xtimes, wave_signal_float)
##plt.grid()
##plt.show()
## filter the signal,,, begin
#    length_wave_signal_float= len(wave_signal_float)
#    print 'length_wave_signal_float=',length_wave_signal_float
#    print 'framerate=',framerate
#    s=wave_signal_float
#    t_total=length_wave_signal_float/framerate
#    print 't_total=',t_total
##plt.plot(xtimes, s)
## filter the signal,,, end
## close the open wave file
#    file_read.close()
#    word_start_time, word_end_time = good_read_xml_1(filename_1,word)
##print 'word_start_time=', word_start_time
##print 'word_end_time=', word_end_time
#    word_start_point = word_start_time*framerate
#    word_end_point=word_end_time*framerate
#    return wave_signal_float,framerate, word_start_point, word_end_point
##print word_start_point
##print word_end_point 
#
#
#
#
#
#
## save result of a wave file
##
##filename = 'out_01_filter1.wav'
##mode     = 'wb' 
##file_write       = wave.open(filename,mode)
##
##file_write.setframerate(framerate)
##file_write.setnchannels(nchannels)
##file_write.setsampwidth(sampwith)
##
### reconversion into string
##wave_signal_int16 = wave_signal_float.astype(int16)
##wave_signal_string= wave_signal_int16.tostring()
###print type(wave_signal_string)
##
##file_write.writeframes(b''.join(wave_signal_string))
##file_write.close()
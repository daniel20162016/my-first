# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 10:27:32 2016

@author: wang
"""
#import numpy
import numpy as np

#a=[1,2,3,4,45,9,8,5,2]
#b=[10,20,30]
##np.savetxt('new.csv', a,delimiter = ',')
#np.savez('c.npz',a,b)

r=np.load('je_compare.npz')
#print 'matrix_1=',r["arr_0"] # this is the first matrix
print 'matrix_5=',r["arr_4"] # this is the second matrix
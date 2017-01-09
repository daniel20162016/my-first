# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:45:22 2016

@author: wang
"""
import numpy as np
from math import sqrt

origin=np.load('un_192_matrix.npz')
#print 'r_matrix_1=',origin["arr_0"] # this is the first matrix
#print 'r_matrix_2=',r["arr_1"] # this is the second matrix
#print r["arr_0"] [23][7]

test=np.load('un_compare_192_matrix.npz')

def multipl(a,b):
    sumofab=0.0
    for i in range(len(a)):
        temp=a[i]*b[i]
        sumofab+=temp
    return sumofab
    
def corrcoef(x,y):
    n=len(x)
    #求和
    sum1=sum(x)
    sum2=sum(y)
    #求乘积之和
    sumofxy=multipl(x,y)
    #求平方和
    sumofx2 = sum([pow(i,2) for i in x])
    sumofy2 = sum([pow(j,2) for j in y])
    num=sumofxy-(float(sum1)*float(sum2)/n)
    #计算皮尔逊相关系数
    den=sqrt((sumofx2-float(sum1**2)/n)*(sumofy2-float(sum2**2)/n))
    return num/den
 
#x = [0,1,0,3]
#y = [0,1,1,1]
 #print corrcoef(x,y) #0.471404520791

x_database_1=origin["arr_0"]
x_database_2=origin["arr_1"]
x_database_3=origin["arr_2"]
x_database_4=origin["arr_3"]
x_database_5=origin["arr_4"]

y_test_1=test["arr_0"]
y_test_2=test["arr_1"]
y_test_3=test["arr_2"]
y_test_4=test["arr_3"]
y_test_5=test["arr_4"]

corrcoef_all=np.zeros([25])

corrcoef_all[0]=corrcoef(y_test_1,x_database_1)
corrcoef_all[1]=corrcoef(y_test_1,x_database_2)
corrcoef_all[2]=corrcoef(y_test_1,x_database_3)
corrcoef_all[3]=corrcoef(y_test_1,x_database_4)
corrcoef_all[4]=corrcoef(y_test_1,x_database_5)

corrcoef_all[5]=corrcoef(y_test_2,x_database_1)
corrcoef_all[6]=corrcoef(y_test_2,x_database_2)
corrcoef_all[7]=corrcoef(y_test_2,x_database_3)
corrcoef_all[8]=corrcoef(y_test_2,x_database_4)
corrcoef_all[9]=corrcoef(y_test_2,x_database_5)

corrcoef_all[10]=corrcoef(y_test_3,x_database_1)
corrcoef_all[11]=corrcoef(y_test_3,x_database_2)
corrcoef_all[12]=corrcoef(y_test_3,x_database_3)
corrcoef_all[13]=corrcoef(y_test_3,x_database_4)
corrcoef_all[14]=corrcoef(y_test_3,x_database_5)

corrcoef_all[15]=corrcoef(y_test_4,x_database_1)
corrcoef_all[16]=corrcoef(y_test_4,x_database_2)
corrcoef_all[17]=corrcoef(y_test_4,x_database_3)
corrcoef_all[18]=corrcoef(y_test_4,x_database_4)
corrcoef_all[19]=corrcoef(y_test_4,x_database_5)

corrcoef_all[20]=corrcoef(y_test_5,x_database_1)
corrcoef_all[21]=corrcoef(y_test_5,x_database_2)
corrcoef_all[22]=corrcoef(y_test_5,x_database_3)
corrcoef_all[23]=corrcoef(y_test_5,x_database_4)
corrcoef_all[24]=corrcoef(y_test_5,x_database_5)

print corrcoef_all

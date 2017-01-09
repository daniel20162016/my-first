# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:45:22 2016

@author: wang
"""
import numpy as np
from math import sqrt

#origin=np.load('je_le_qui_dans_de_192_matrix.npz')
##print 'r_matrix_1=',origin["arr_0"] # this is the first matrix
##print 'r_matrix_2=',r["arr_1"] # this is the second matrix
##print r["arr_0"] [23][7]
#
#test=np.load('je_le_qui_dans_de_192_matrix_compare.npz')

def matrix_compare_pearson_5_mots_good_def(origin, test):
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
#print corrcoef_all
    je_result= np.sort(corrcoef_all)
    je_result_average_1_values=je_result[24]
#print je_result
    je_result_average_3_values = (je_result[24] + je_result[23] + je_result[22])/3
#print 'three values average_je_=',je_result_average_3_values
#print 'the first value_je_=',je_result_average_1_values
    

#==============================================================================
# this part is for  le
#==============================================================================

    x_database_1=origin["arr_5"]
    x_database_2=origin["arr_6"]
    x_database_3=origin["arr_7"]
    x_database_4=origin["arr_8"]
    x_database_5=origin["arr_9"]

    y_test_1=test["arr_5"]
    y_test_2=test["arr_6"]
    y_test_3=test["arr_7"]
    y_test_4=test["arr_8"]
    y_test_5=test["arr_9"]

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
#print corrcoef_all
    le_result= np.sort(corrcoef_all)
    le_result_average_1_values=le_result[24]
#print je_result
    le_result_average_3_values = (le_result[24] + le_result[23] + le_result[22])/3
#print 'three values average_le_=',le_result_average_3_values
#print 'the first value_le_=',le_result_average_1_values


#==============================================================================
#  this part is for qui
#==============================================================================


    x_database_1=origin["arr_10"]
    x_database_2=origin["arr_11"]
    x_database_3=origin["arr_12"]
    x_database_4=origin["arr_13"]
    x_database_5=origin["arr_14"]

    y_test_1=test["arr_10"]
    y_test_2=test["arr_11"]
    y_test_3=test["arr_12"]
    y_test_4=test["arr_13"]
    y_test_5=test["arr_14"]

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
#print corrcoef_all
    qui_result= np.sort(corrcoef_all)
    qui_result_average_1_values=qui_result[24]
#print je_result
    qui_result_average_3_values = (qui_result[24] + qui_result[23] + qui_result[22])/3
#print 'three values average_qui_=',qui_result_average_3_values
#print 'the first value_qui_=',qui_result_average_1_values

#==============================================================================
#  dans
#==============================================================================


    x_database_1=origin["arr_15"]
    x_database_2=origin["arr_16"]
    x_database_3=origin["arr_17"]
    x_database_4=origin["arr_18"]
    x_database_5=origin["arr_19"]

    y_test_1=test["arr_15"]
    y_test_2=test["arr_16"]
    y_test_3=test["arr_17"]
    y_test_4=test["arr_18"]
    y_test_5=test["arr_19"]

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
#print corrcoef_all
    dans_result= np.sort(corrcoef_all)
    dans_result_average_1_values=dans_result[24]
#print je_result
    dans_result_average_3_values = (dans_result[24] + dans_result[23] + dans_result[22])/3
#print 'three values average_dans_=',dans_result_average_3_values
#print 'the first value_dans_=',dans_result_average_1_values

#==============================================================================
# this part is for de
#==============================================================================


    x_database_1=origin["arr_20"]
    x_database_2=origin["arr_21"]
    x_database_3=origin["arr_22"]
    x_database_4=origin["arr_23"]
    x_database_5=origin["arr_24"]

    y_test_1=test["arr_20"]
    y_test_2=test["arr_21"]
    y_test_3=test["arr_22"]
    y_test_4=test["arr_23"]
    y_test_5=test["arr_24"]

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
#print corrcoef_all
    de_result= np.sort(corrcoef_all)
    de_result_average_1_values=de_result[24]
#print je_result
    de_result_average_3_values = (de_result[24] + de_result[23] + de_result[22])/3
#print 'three values average_de_=',de_result_average_3_values
#print 'the first value_de_=',de_result_average_1_values

    result_total_first_value =  ( je_result_average_1_values+le_result_average_1_values+qui_result_average_1_values+dans_result_average_1_values+de_result_average_1_values )/5
#    print 'first_value =',result_total_first_value

    result_total_three_value = (je_result_average_3_values + le_result_average_3_values + qui_result_average_3_values + dans_result_average_3_values + de_result_average_3_values)/5
#    print 'total_three_value =',result_total_three_value
    return result_total_first_value, result_total_three_value
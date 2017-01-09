# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:45:22 2016

@author: wang
"""
import numpy as np
from math import sqrt
from matrix_compare_pearson_5_mots_good_def import*

from calcul_matrix_je_le_qui_dans_de_192_matrix_def_good import*
from calcul_matrix_je_le_qui_dans_de_192_matrix_compare_df_good import*

# open a wave file
#==============================================================================
# this is the first conversation
#==============================================================================
filename = 'francois_filon_pure_1.wav'
filename_1 ='francois_filon_pure_1.xml'

#==============================================================================
# this is the second conversation
#==============================================================================
filename_2 = 'francois_filon_pure_3.wav'
filename_3 ='francois_filon_pure_3.xml'


#==============================================================================
# the five words that we choosed
#==============================================================================
word ='je'
word_2='le'
word_3='qui'
word_4='dans'
word_5='de'


#==============================================================================
# when calcul_matrix_je_le_qui_dans_de_192_matrix_def_good is finished, we get the database of je_le_qui_dans_de_192_matrix.npz
#==============================================================================
finish = calcul_matrix_je_le_qui_dans_de_192_matrix_def_good(filename, filename_1,word,word_2,word_3,word_4,word_5)
print 'finish=',finish


#==============================================================================
# when calcul_matrix_je_le_qui_dans_de_192_matrix_compare_df_good is finished, we get the database of 'je_le_qui_dans_de_192_matrix_compare.npz'
#==============================================================================
finish_2=calcul_matrix_je_le_qui_dans_de_192_matrix_compare_df_good(filename_2, filename_3,word,word_2,word_3,word_4,word_5)
print 'finish_2=',finish

origin=np.load('je_le_qui_dans_de_192_matrix.npz')
test=np.load('je_le_qui_dans_de_192_matrix_compare.npz')


result_total_first_value, result_total_three_value = matrix_compare_pearson_5_mots_good_def(origin, test)
 
print 'maximum_value =',result_total_first_value
print 'three_values_average =',result_total_three_value




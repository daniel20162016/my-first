##coding=utf-8
#import  xml.dom.minidom
#from numpy import*
#import sys
#

#def read_xml_try_3(filename,word_chose):
#    dom = xml.dom.minidom.parse(filename)
#    root = dom.documentElement
#    itemlist = root.getElementsByTagName('word')   
##filename = sys.argv[1]
##dom = xml.dom.minidom.parse('francois_filon_pure_1.xml')
#    length_word = len(itemlist)
#    je='word_chose'
#    number_of_je = 5 # this is define how many 'word' that we will use in the database
#    je_start=zeros([number_of_je],dtype='float')
#    je_length=zeros([number_of_je],dtype='float')
#    je_end=zeros([number_of_je],dtype='float')
#    number_count=0
#    for i in range (0, length_word):
#        item=itemlist[i]
#        value_i=item.getAttribute("value")
#        if je==value_i:
#            length_i=item.getAttribute("length")
#            je_start[number_count]=float(item.getAttribute("start"))
#            je_end[number_count]=je_start[number_count]+je_length[number_count]
#            number_count=number_count+1
#            if number_count==number_of_je:
#                break       
#print je_start
#print je_end
#return je_start, je_end        

from good_read_xml_1 import*
filename_1 ='francois_filon_pure_1.xml'
word ='je'

word_start, word_end = good_read_xml_1(filename_1,word)

print 'word_start=', word_start
print 'word_end=', word_end
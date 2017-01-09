#coding=utf-8
import  xml.dom.minidom
from numpy import*
import sys


def read_xml_try_3(filename,word):
    dom = xml.dom.minidom.parse(filename)
    root = dom.documentElement
    itemlist = root.getElementsByTagName('word')   
#filename = sys.argv[1]
#dom = xml.dom.minidom.parse('francois_filon_pure_1.xml')
    length_word = len(itemlist)
    number_of_word = 5 # this is define how many 'word' that we will use in the database
    word_start=zeros([number_of_word],dtype='float')
    word_length=zeros([number_of_word],dtype='float')
    word_end=zeros([number_of_word],dtype='float')
    number_count=0
    for i in range (0, length_word):
        item=itemlist[i]
        value_i=item.getAttribute("value")
        if word==value_i:
            length_i=item.getAttribute("length")
            word_start[number_count]=float(item.getAttribute("start"))
            word_length[number_count]=float(item.getAttribute("length"))            
            word_end[number_count]=word_start[number_count]+word_length[number_count]
            number_count=number_count+1
            if number_count==number_of_word:
                break       
#    print je_start
#    print je_end
    return word_start, word_end        

###coding=utf-8
##import  xml.dom.minidom
##
###打开xml文档
##dom = xml.dom.minidom.parse('abc.xml')
###
####得到文档元素对象
##root = dom.documentElement
##
##cc=dom.getElementsByTagName('caption')
##c1=cc[0]
##print c1.firstChild.data
##
##c2=cc[1]
##print c2.firstChild.data
##
##c3=cc[2]
##print c3.firstChild.data
#
#
##coding=utf-8
##from xml.etree import ElementTree as ET
##per=ET.parse('abc.xml')
##p=per.findall('./login/item')
##
##
##
##for oneper in p:
##    for child in oneper.getchildren():
##        print child.tag,':',child.text
##
##
##p=per.findall('./item')
##
##for oneper in p:
##    for child in oneper.getchildren():
##        print child.tag,':',child.text
#
#
#import  xml.dom.minidom
#
##打开xml文档
#dom = xml.dom.minidom.parse('abc.xml')
#
##得到文档元素对象
#root = dom.documentElement
#
#bb = root.getElementsByTagName('caption')
#b= bb[2]
#print b.nodeName
#
#bb = root.getElementsByTagName('item')
#b= bb[1]
#print b.nodeName


import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('abc.xml')

#得到文档元素对象
root = dom.documentElement

itemlist = root.getElementsByTagName('login')
item = itemlist[0]
un=item.getAttribute("username")
print un


pd=item.getAttribute("passwd")
print pd
#
#ii = root.getElementsByTagName('item')
#i1 = ii[0]
#i=i1.getAttribute("id")
#print i
#
#i2 = ii[1]
#i=i2.getAttribute("id")
#print i
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:35:47 2019

@author: Bhavya
"""

import PyPDF2

PDFFile = open("file.pdf",'rb')

PDF = PyPDF2.PdfFileReader(PDFFile)
pages = PDF.getNumPages()
key = '/Annots'
uri = '/URI'
ank = '/A'
counter= 0

for page in range(pages):
    #print("Current Page: {}".format(page))
    pageSliced = PDF.getPage(page)
    pageObject = pageSliced.getObject()
    if key in pageObject.keys():
        ann = pageObject[key]
        for a in ann:
            u = a.getObject()
            if uri in u[ank].keys():
                print(counter,u[ank][uri])
                counter+=1
                
print(counter)
    
# -*- coding: utf-8 -*-
"""

@author: Rens van Dam

Election program scraping


GOAL:
    
1. Scrape election programs for certain keywords
2. Compare them directly
3. Graph the results

"""

import pdfplumber
import glob
import matplotlib.pyplot as plt


#puts all pdf files into an array:
#pdffiles = []
#for file in glob.glob("*.pdf"):
#    pdffiles.append(file)
#print(pdffiles)


def scrapepdf(word):
    
    amountpages = []
    amounttotal = []
    amountword = []
    
    #puts all pdf files into an array
    pdffiles = []
    for file in glob.glob("*.pdf"):
        pdffiles.append(file)
        
    #open a PDF file of your choosing
    for pdffile in pdffiles:
        with pdfplumber.open(pdffile) as pdf: 
            with open(pdffile+".txt", 'w', encoding = "unicode_escape") as f:
            
                amountpages.append(len(pdf.pages))
                for i in range(0,len(pdf.pages)-1):
                    f.write(pdf.pages[i].extract_text())
                    
            with open(pdffile+".txt", 'r') as f:
                text = f.read()
                
                comb = str(word)
                n = text.count(comb)
                total = len(text.split())
                amounttotal.append(total)
                amountword.append(n)
                
    print(amountpages, amounttotal, amountword)
    
    names = [filename.replace('.pdf', '') for filename in pdffiles]
    
    plt.figure(figsize=(10,6))
    plt.bar(names,amountword)
    plt.title("occurrence rate")
    plt.xlabel('pdf file')
    plt.ylabel('occurrences')
    plt.show()
       
                
scrapepdf("studenten")
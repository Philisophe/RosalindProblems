#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 18:03:23 2018

@author: kalashnikov
"""

#This one counts the number of nucleotides of every kind
def count_nuc (st):
    results = [0,0,0,0]
    for i in st:
        if i == 'A':
            results[0] = results[0]+1
        if i == 'C':
            results[1] = results[1]+1
        if i == 'G':
            results[2] = results[2]+1
        if i == 'T':
            results[3] = results[3]+1
    print (str(results[0]) + " " + str(results[1]) + " " +str(results[2]) + " " + str(results[3]))
    
#Another option
    def count_nuc2(s):
         return s.count("A"), s.count("G"), s.count("C"), s.count("T")


# Replaces every nucleotide with a different one
def DNAtoRNA(s):
    return s.replace("T", "U")

# Produces the reversed compliment (A to T, G to C, ...; then reverse the string)
def rev_comp(s):
    l = list(s)
    p = 0
    for i in l:
        if i == 'A':
            l[p] = 'T'
        if i == 'T':
            l[p] = 'A'
        if i == 'C':
            l[p] = 'G'
        if i == 'G':
            l[p] = 'C'
        p=p+1
    print (l)
    l = l[::-1]
    s = "".join(l)
    return s
    
# A better version
    st = "AAAACCCGGT"
    st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
    print (st)
    
# Or
    from string import maketrans
    s = 'AAAACCCGGT'
    print(s[::-1].translate(maketrans('ACGT', 'TGCA')))
    
    
"""   
def GC(file):
    s = open(file).read()
    s = s.replace(' ', '').replace('\n', '') # Let's get rid of all spaces and newline-characters
    numStr = s.count('Rosalind')# How many entries are there?
    print("numStr ",numStr, '\n\n')
    dic = {}
    w=1 
    for i in range(numStr):
        print (" this is i ", i)
        print ('this is w ', w)
        RosInd = s.find('Rosalind', w) # The closest entry, starting with "Rosalind..."
        print(" this is RosInd ", RosInd)
        w = w+RosInd+1
        print ("this is s[w] - ",s[w])
        dnaStr = s[RosInd+14:s.find('>',RosInd+14)] # The string of nucleotides of this entry
        #print("Dnastr", dnaStr)
        dic[s[RosInd:RosInd+13]] = round(((dnaStr.count('G') + dnaStr.count('C'))/len(dnaStr)),7)*100
        print (" this is dic ", dic)
        print()
    for key, val in dic.items():
        print (key, "\n", val, '\n')
    return
"""

# Computes the GC content of the string    
def GC2(file):
    import re
    s = open(file).read()
    s = s.replace(' ', '').replace('\n', '') # Let's get rid of all spaces and newline-characters
    RosInd = [m.start() for m in re.finditer('Rosalind', s)]
    name = []
    GCC = []
    lr = len(RosInd)
    for i in range(lr):
        name.append(s[RosInd[i]:RosInd[i]+13])
        if i==lr-1:
            GCC.append(s[RosInd[i]+13:])
        else:
            GCC.append(s[RosInd[i]+13:RosInd[i+1]-1])
    for i in range(lr):
        GCC[i] = (GCC[i].count('C')+GCC[i].count('G'))/len(GCC[i])*100
    for i in range(lr):
        print (name[i],GCC[i])
    return
            
    
    
    
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Splits the text making a list with the letters.
text = open('/Users/miriamplanchat/Desktop/Cristi/GRAU_FISICA/Semestre_7/Teoria_Informacio/Avaluacio_Continuada/quijote.txt').read()
letter_list = text.split()

Compression_dict = {}

k = 1
j = 0
finish_flag = 1 

while finish_flag == 1: 

    strtosearch =  letter_list[j]
    
    exist_str_flag = 1 
    while exist_str_flag == 1: 
        if  not strtosearch in Compression_dict.values():
            Compression_dict[k] = strtosearch
            k = k + 1
            exist_str_flag = 0
            j = j + 1
        else:
            strtosearch = strtosearch  + letter_list[j + 1]
            j = j + 1
    if j == len(letter_list):
        finish_flag = 0
                

print(Compression_dict)


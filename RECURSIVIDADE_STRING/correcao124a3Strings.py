# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 08:00:55 2020

@author: lcam
"""

'''
''--> ''
'a' --> 'aa'
'av'--> 'aavv'
'avf'--> 'aavvff'


'''
def replica(s):
    if not s:
        return s
    #res=duplicaprimeiro + replica o resto
    duplica1o= s[0]*2
    replicaResto=replica(s[1:])
    return duplica1o+replicaResto

'''
'', 'g' --> False
'.','g' --> False ou True
'..','g' -->  se o 1º é 'g' -->True
'''
def temCar(s,c):
    if not s:
        return False
    #if len(s) == 1:
    #    return s[0]==c
    if s[0] == c:
        return True
    resp=temCar(s[1:])
    return resp
        

def temVogal(s):
    if not s:
        return False
    #if len(s) == 1:
    #    return s[0]==c
    if s[0] in 'aeiouAEIOU':
        return True
    resp=temCar(s[1:])
    return resp

'''
4.a) '' + '' --> ''
    'a' + 'b' --> 'a'+'b'
    'aA' + 'bB' --> 'ab' + intercalação do resto
    'aAc' + bBd' -->  'ab' + intercala o restante
'''
def intercalaA(s1,s2):
    if s1=='':  # são de mesmo tamanho
        return ''
    primS1= s1[0]
    primS2= s2[0]
    resto= intercalaA(s1[1:],s2[1:])
    return primS1+primS2+resto
    

















    
    
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:11:18 2020

@author: sn381
"""


filename=input("File to be encrypted or decrypted:")

k=input('What key is to be used:')

operator=input("decrypt(D) or encrypt(E):")


               
if operator=='E':               
               
    f=open(filename,'r')
    x=f.read()


    key =k
    word_key=[]


    count_key=0
    count_f=0

    for i in x:
        count_f+=1
        count_key+=1
        word_key.append(key[count_key-1])
        if count_key==len(key):
        
            count_key=0


    asc_key=[]

    for l in word_key:
        asc_key.append(ord(l))
    
    
    subtract_key=[]

    for t in asc_key:
    
        subtract_key.append(t-32)
    
    
    asc_text=[]

    count_cipher=0
    for z in x:
        count_cipher+=1
    
        if (ord(z)+subtract_key[count_cipher-1])>126:
            asc_text.append((ord(z)+subtract_key[count_cipher-1])-95)
        else:
            asc_text.append(ord(z)+subtract_key[count_cipher-1])
        
       
        
    cipher_text=''
    

    for s in asc_text:
        cipher_text+=chr(s)
    
    encrypted= open('enc_'+filename,"w+")

    encrypted.write(cipher_text)


    encrypted.close()
    f.close()

if operator=='D':
    f=open(filename,'r')
    x=f.read()

    key=k

    counter=0
    counter1=0

    repeated_key=[]

    for i in x:
        counter+=1
        counter1+=1
        repeated_key.append(key[counter1-1])
        if counter1==len(key):
            counter1=0
    
    
    asc_repeated=[]

    for l in repeated_key:
        asc_repeated.append(ord(l)-32)

    decrypted=[]

    count=0
    for t in x:
        count+=1
    
        if (ord(t)-asc_repeated[count-1])<32:
            decrypted.append((ord(t)-asc_repeated[count-1])+95)
        else:
            decrypted.append((ord(t)-asc_repeated[count-1]))
    
    
    
    dec=open('dec_'+filename,"w+")

    plain=''

    for d in decrypted:
        plain+=chr(d)
    
    dec.write(plain)
    

    dec.close()
    f.close()



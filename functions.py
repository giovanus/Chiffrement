# -*- coding: utf-8 -*-
import string
def crypter(message,key):
    message=message.upper()
    key=key.upper()
    keys={}
    idx=0
    for letter in key :
        keys[idx]=ord(letter)-65
        idx+=1
    crypt=''
    indice=0
    char_code=0
    dif=0
    for letter in message:
        if letter==' ':
            crypt+=' '
        else:
            if indice==len(key):
                indice=0
            if ord(letter)+keys[indice]>90 :
                dif=(ord(letter)+keys[indice])-90
                char_code=64+dif
            else:
                char_code=ord(letter)+keys[indice]
            crypt+=chr(char_code)
            indice+=1
    return crypt

def cryptFromFile(Dir,key):
    ofi=open(Dir,'r')
    message=ofi.read()
    ofi.close()
    crypt_message=crypter(message, key)
    return crypt_message
def keyChecker(key):
    for letter in key :
        if letter not in string.ascii_letters :
            return False
    return True
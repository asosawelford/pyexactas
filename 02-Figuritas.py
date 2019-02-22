# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:23:33 2019

@author: aleja
"""
import random 
import numpy as np

def generar_figurita(n):
    return random.randint(1,n)

def album_6():
    count=0
    album=[]
    while len(album) != 6:
        figu=generar_figurita(6)
        if figu not in album:
            album.append(figu)
        count += 1
    return count
            
def cuantas_figus(figus_total):
    count=0
    album=[]
    while len(album) != figus_total:
        figu=generar_figurita(figus_total)
        if figu not in album:
            album.append(figu)
        count += 1
    return count

def mean_album6():
    resultados=[]
    i=0
    while i < 1000:
        resultados.append(album_6())
        i += 1
    return np.mean(resultados)

def mean_album(figus_total):
    resultados=[]
    i=0
    while i < 100:
        resultados.append(cuantas_figus(figus_total))
        i += 1
    return np.mean(resultados)



""" 
"""
def paquete5():
    paquete_5=[]
    i=0
    while i < 5:
        paquete_5.append(random.randint(1,669))
        i += 1
    return paquete_5

def paqueten(figus_total,figus_paquete):
    paquete_n=[]
    i=0
    while i < figus_paquete:
        paquete_n.append(random.randint(1,figus_total))
        i += 1
    return paquete_n

def cuantos_paquetes(figus_total,figus_paquete):
    count = 0
    album=[]
    while len(album) < figus_total:
        paquete=paqueten(figus_total,figus_paquete)
        for i in paquete:
            if i not in album:
                album.append(i)
        count += 1
    return count

def mean_n(figus_total,figus_paquete,rep):
    i = 0
    lista = []
    for i in range (rep):
        lista.append(cuantos_paquetes(figus_total,figus_paquete))
    return np.mean(lista)

            
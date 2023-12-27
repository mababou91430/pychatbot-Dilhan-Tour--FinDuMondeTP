from IDF import *
from Fonction_ines import *
import os
#from TF_IDF import*


def nom_president():
    L = []
    remplacement = "'!?123456789"
    for filename in os.listdir("speeches-20231124"):
        for i in range(len(remplacement)):
            filename = filename.replace(remplacement[i],     "")
        filename = filename.replace("Nomination_", "")
        filename = filename.replace(".txt", "")
        if filename not in L:
            L.append(filename)
    return L


def clean():
    for filename in os.listdir("speeches-20231124"):
        mon_fichier = "speeches-20231124/" + filename
        f1 = open(mon_fichier, "r")
        repertoire_nom_fichier = "cleaned/" + filename
        f = open(repertoire_nom_fichier, "w")
        ligne = f1.readline()
        while ligne != "":
            l = list(ligne)
            for i in range(len(ligne)):
                if 65 <= ord(l[i]) <= 90:
                    l[i] = chr(ord(l[i]) + 32)
            ligne = "".join(l)
            f.write(ligne)
            ligne = f1.readline()


def corpus(x):
    k=[]
    j=Tokenisation(x)
    print(j)
    for filename in os.listdir("cleaned"):
        text = "cleaned/" + filename
        f1 = open(text, "r",encoding="utf-8")
        ligne = f1.readline()
        d = TF(text)
        print(d)
        for elem in j:
            print(elem)
            if elem in d and elem not in k:
                    k.append(elem)
    return("les mots présents dans le corpus et la question sont :",k)

def Tokenisation(text):
    l = list(text)
    for i in range(len(l)):
        if 65 <= ord(l[i]) <= 90:
            l[i] = chr(ord(l[i]) + 32)
        if (33 <= ord(l[i]) <= 47) or (58 <= ord(l[i]) <= 64) or (91 <= ord(l[i]) <= 96) or (123 <= ord(l[i]) <= 126):
            if ord(l[i]) == 45 or 39:
                l[i] = chr(32)
            else:
                l.remove(l[i])
    question = "".join(l)
    question = question.split(" ")
    return question


def vecteur_TF_IDF(text):
    g = {}
    mop = []
    test = False
    TF_IDF_Inverser = []
    l = Tokenisation(text)
    b = TF_IDF()
    nb_mots = 0
    for i in range(len(l)):
        if l[i] != "" and l[i] !=" ":
            nb_mots += 1
    for i in range(len(l)):
        if l[i] != "" and l[i] !=" ":
            g[l[i]] = l.count(l[i])
    d = IDF()
    for i in d.keys():
        test = False
        for j in g.keys():
            if i == j:
                d[i] = g[i]*d[i]
                test = True
        if test == False:
            d[i] = 0
    for i in d.keys():
        mop.append(d[i])
    return mop

text = "présidents messieurs Ceci est une question de test pour savoir si le code que j'ai fait marche une question est une question climat président messieurs messieurs"
#print(vecteur_TF_IDF(text))

import math


def similarite(A, B):
    c = 0
    m = produit_scalaire(A,B)
    n = normeM(A)
    p = normeM(B)
    c = m /(n * p)
    return c

def produit_scalaire(A, B):
    c = len(TF_IDF())
    r = 0
    for i in range(c):
        r += float(A[i])*float(B[i])
    return r

def normeM(A):
    r = 0
    for i in range(len(A)):
        r += float(A[i])**2
    return math.sqrt(r)

def document_pertinent(TFIDF,vecteur_question,nom_text):
    temp = 0.0
    document = 0
    for i in range(8):
        d = similarite(vecteur_question,TFIDF[i])
        if float(d) > temp:
            temp = d
            document = i
    g = nom_text[document]
    return g







list_text = []
for filename in os.listdir("cleaned"):
    list_text.append(filename)
bn = vecteur_TF_IDF(text)
TF_IDF_Inverser = []
l = Tokenisation(text)
b = TF_IDF()
nb_mots = 0
for i in range(1,9):
    L = []
    for j in range(len(b)):
        L.append(b[j][i])
    TF_IDF_Inverser.append(L)
g = vecteur_TF_IDF(text)
print(document_pertinent(TF_IDF_Inverser,bn,list_text))

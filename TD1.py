def sum(n): # utilise les types des objets
    a=str(2**n) 
    l=len(a)
    s=0
    for i in range(l):
        s+=int(a[i])
    return s
    
def sum1(n): # utilise la division euclidienne
    a=2**n
    s=0
    while a!=0 :
        s += a%10
        a = (a-a%10)//10
    return s

assert(sum1(15) == 26)


import os
os.chdir('C:\\Users\\bulou\\Desktop\\Oregane')
f=open("names.txt",'r')
names=f.read()
f.close()


def ListeTriee(fichier):
    lis=fichier.split(',')
    return(sorted(lis)) #utilisation de return pour avoir une liste en sortie et pas un objet Nonetype
    
namesTri = ListeTriee(names)

# def score(tab): 
#     res = [0]*len(tab) 
#     k=1
#     for nom in tab:#on fait le score de chaque nom
#         n=len(nom) #longueur du nom
#         s=0 # on initialise le score à 0 pour chaque nom
#         for i in range(n):
#             s +=ord(nom[i])-ord('A')+1 #on "additionne" les lettres
#             res[k-1] = k*s
#         k+=1
#     return res
    
def score2(tab):
    res = [0]*len(tab) 
    k=1
    s=0
    for nom in tab: #on fait le score de chaque nom
        s=SomLet(nom)
        res[k-1] = k*s
        k+=1
    return res

def SomLet(mot):
    n=len(mot)
    s=0
    for i in range(n):
        s += ord(mot[i])-ord('A')+1
    return s


#assert ( score(namesTri)[937]==49714)

#print(score(namesTri))

#ord('let')-ord('a')+1

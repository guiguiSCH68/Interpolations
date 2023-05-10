import math
import copy
import matplotlib.pyplot as plt
import numpy as np

#helper functions
def Mult_poly_poly(P1,P2): # polys [an...a0]
    #on initialise une liste vide 
    produit = [0] * (len(P1) + len(P2) - 1)
    
    #on multiplie chaque terme de P1 par P2
    for i in range(len(P1)):
        for j in range(len(P2)):
            produit[i+j] += P1[i] * P2[j]
    
    return produit

def somme_polynomes(p, q):
    if len(p) == 0:
        return q
    elif len(q) == 0:
        return p
    else:
        n = max(len(p), len(q))
        result = []
        for i in range(n):
            if i >= len(p):
                result.append(q[i])
            elif i >= len(q):
                result.append(p[i])
            else:
                result.append(p[i] + q[i])
        return result
    
def Eval_poly(P,t):
    
    n=len(P)
    valeur=P[n-1] # on affecte la dernière valeur de A
    for i in range(n-2,-1,-1): # on part du rang n-2 ( = av dernière valeur) on s'arrête au range -1 (0 du coup) par pas de -1 
        valeur=(valeur*t)+P[i]
    return valeur

def Mult_poly_reel(P,r): # polys [an...a0]
    
    P_result = []
    
    for elem in P:
        P_result.append(elem*r) #on multiplie l'élément par le réel
    return P_result
#---

def calculer_Li(i, list_x):
    Li=[]
    numPoly=[1.0]
    denom=1.0
    for j in range(len(list_x)):
        if(i!=j):
            denom=denom*(list_x[i]-list_x[j])
            Pj=[1.0,-list_x[j]]
            numPoly=Mult_poly_poly(numPoly,Pj)
    #Li=np.array(numPoly)
    Li=numPoly
    return Mult_poly_reel(Li , 1.0/denom)

 def Hi_prime_xi(i, list_x):
    sum=0.0
    for j in range(len(list_x)):
        if(i!=j):
            sum=sum + 1.0/(list_x[i]-list_x[j])

    return 2.0*sum
  
def calculer_Ki(i, liste_x, liste_fx, liste_fpx):  
    Hi_prime =  Hi_prime_xi(i, liste_x)
    Ki = Mult_poly_reel( [1.0,-liste_x[i]] , liste_fpx[i]-(Hi_prime*liste_fx[i]) )
    Ki[1] += liste_fx[i] #on ajoute le f(xi) du début au terme constant ( polys: [an...a0])
    return Ki #liste de coeffs

def interpol_Hermite(n, liste_xi, liste_F_xi, liste_F_prime_xi):

    les_Qi = []
    #P = []
    for number in range(n+1):
        L = calculer_Li(number, liste_xi)
        H = Mult_poly_poly(L,L)
        K = calculer_Ki(number, liste_xi, liste_F_xi, liste_F_prime_xi)
        Q = Mult_poly_poly(H,K)
        les_Qi.append(Q)
        
    #calcul de P
    P = [0]*len(les_Qi[0])
    #print(les_Qi)
    for elem in range(len(les_Qi)):
        #print("QI_elem",les_Qi[elem])
        P = somme_polynomes(P,les_Qi[elem])
        #print("P",P)
    return P

def Hermite_process(n, liste_xi, liste_F_xi, liste_F_prime_xi):
    
    pol_interpol = interpol_Hermite(n, liste_xi, liste_F_xi, liste_F_prime_xi)
    pts_hermite = []
    
    #calcul du polynôme dérivé
    deriv_pol_interpol = deriver_polynome(pol_interpol)
    #print(liste_xi)
    pol_interpol.reverse()
    deriv_pol_interpol.reverse()
    #calcul des points entre les supports
    for element in np.arange(liste_xi[0],liste_xi[-1]+0.1,0.01):
            pts_hermite.append(element) 

    #evaluation des points tout juste calculés
    interpolation = []
    interpolation_derive = []
    for elem in pts_hermite:
        interpolation.append(Eval_poly(pol_interpol,elem))
        interpolation_derive.append(Eval_poly(deriv_pol_interpol,elem))
    #print(interpolation)
    
    return interpolation, pts_hermite, interpolation_derive, pol_interpol

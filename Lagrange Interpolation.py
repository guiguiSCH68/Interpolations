import copy

def Eval_poly(P,t):
    
    n=len(P)
    valeur=P[n-1] # on affecte la dernière valeur de A
    for i in range(n-2,-1,-1): # on part du rang n-2 ( = av dernière valeur) on s'arrête au range -1 (0 du coup) par pas de -1 
        valeur=(valeur*t)+P[i]
    return valeur

def Add_deux_polys(P1,P2):
    
    P_result = []
    
    if P1 == []:
        return P2
    elif P2 == []:
        return P1
    else:
        for elem in P1:
            idx = P1.index(elem) # on récupère l'index de l'élément de la première liste
            P_result.append(elem + P2[idx]) # on ajoute la somme entre l'élément de la première liste et l'élément se trouvant au même index dans la seconde    
    return P_result

def Mult_poly_reel(P,r):
    
    P_result = []
    
    for elem in P:
        P_result.append(elem*r) #on multiplie l'élément par le réel
    return P_result

def Mult_poly_poly(P1,P2):
    #on initialise une liste vide 
    produit = [0] * (len(P1) + len(P2) - 1)
    
    #on multiplie chaque terme de P1 par P2
    for i in range(len(P1)):
        for j in range(len(P2)):
            produit[i+j] += P1[i] * P2[j]
    
    return produit

def Interpol_Lagrange(X,Y):  # X : les points du support, Y: les f(X) correspondants
    
    resultat = []
    
    #on récupère la liste des Xj pour pouvoir calculer chaque Li(x)
    for elemX, elemY in zip(X,Y): #on itère sur X et Y en même temps
        denominateur = 1
        numerateur = [1]
        temp_listeX = copy.deepcopy(X)#on copie la liste des X
        idx = X.index(elemX)
        del(temp_listeX[idx]) # on supprime le Xi qu'on ne va pas utiliser dans le dénominateur 
    
        #calcul des (x-Xj)/(Xi-Xj)
        for element in temp_listeX:
            numerateur = Mult_poly_poly(numerateur,[-element, 1])#on multiplie le numérateur obtenu par l'actuel (sous forme de liste de coefficients) 
            denominateur *= (elemX-element) # de même pour le dénominateur 
        
        #on récupère et on calcule le couple f(Xi)Li(x) actuel
        couple_fxi_Li = Mult_poly_reel(numerateur, elemY/denominateur)#on "extrait" le dénominateur du Li(x) afin d'avoir uniquement 1 appel de cette fonction à faire
        
        #on ajoute le résultat l'actuel aux précédents calculés
        resultat = Add_deux_polys(couple_fxi_Li,resultat )
    return resultat   

def interpol_Lagrange_process(liste_support,liste_valeurs): 
    
    resultat = Interpol_Lagrange(liste_support,liste_valeurs)
    X_pts_lagrange = []
        
    #calcul des points entre les supports
    for element in np.arange(liste_support[0],liste_support[-1]+0.1,0.10):
            temp = np.float32(element)
            X_pts_lagrange.append(temp) 
            #print(X_pts_lagrange)

    #evaluation des points tout juste calculés
    interpolation = []
    for elem in X_pts_lagrange:
        interpolation.append(Eval_poly(resultat,elem))
        
    return interpolation, X_pts_lagrange

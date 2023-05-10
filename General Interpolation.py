def Tab_diff_div(X,Y):
    if(len(X)==1):
        return Y[0]
    else:
        nom = Tab_diff_div(X[1:len(X)], Y[1:len(Y)]) - Tab_diff_div(X[0:len(X)-1], Y[0:len(Y)-1])
        den = (X[-1]-X[0])
        return nom/den

def EvalH(C,A,t):
  
    n=len(A)
    valeur=A[n-1] # on affecte la dernière valeur de A
    for i in range(n-2,-1,-1): # on part du rang n-2 ( = av dernière valeur) on s'arrête au range -1 (0 du coup) par pas de -1 
        valeur=valeur*(t-C[i])+A[i]
    return valeur

#comptutes the interpolation polynomial
def Interpol(n,X,Y): # il faut que X contienne n+1 "points" pour pouvoir interpoler 
    
    if (len(X) != n+1): # erreur si trop ou pas assez de points.
        return "ERROR"
    
    p = [[],[]]
        
    p[0] = X # les points sont eux-mêmes les centres ici.
    
    p[1] = []
    for i in range(1,len(X)+1):
        p[1].append(Tab_diff_div(X[:i],Y[:i])) # création d'une liste contenant les coeffs nécéssaires pour la formule de Newton lors de l'interpolation
    
    return p

#computes the acutal interpolation curb
def interpol_process(liste_support,liste_valeurs): 
    
    resultat = Interpol(len(liste_support_initial)-1,liste_support,liste_valeurs)

    X_pts = []
        
    #calcul des points entre les supports
    for element in np.arange(liste_support[0],liste_support[-1],10):
            temp = np.float32(element)
            temp2 = np.float64(element)
            X_pts.append(temp) 

    #evaluation des points tout juste calculés
    interpolation = []
    for elem in X_pts:
        interpolation.append(EvalH(liste_support,resultat[1],elem))
    return interpolation, X_pts
  

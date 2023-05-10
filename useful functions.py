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
  
 

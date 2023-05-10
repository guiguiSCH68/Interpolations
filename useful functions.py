import matplotlib.pyplot as plt

interpolation_initiale = interpol_process(liste_support_initial, liste_valeur_initial)

#template for plotting an interpolation

plt.plot(interpolation_initiale[1],interpolation_initiale[0], label = 'interrpolation')
plt.plot(liste_support_initial,liste_valeur_initial,label = "points du support")
plt.xlabel('x')
plt.ylabel(' y')
plt.title('Interpolation')
plt.grid()
plt.show()

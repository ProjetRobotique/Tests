from tkinter import *
 
# fenêtre principale
w = Tk()
w.title("C'est bien parti pour le 100/100")
w.geometry("720x575")
w.config(background='#41B77F')

#texte
label_title = Label(w, text="Bienvenue sur cette fenêtre inutile", font = ("",20), bg='#41B77F', fg='white')
label_title.pack(side=BOTTOM)
 
# matrice à deux dimensions
tableau = []
for i in range(25):
    tableau.append([0] * 25)
 
# les 2 couleurs à utiliser
couleurs = {0: "white", 1: "#41B77F"}
 
# dimensions du canevas
can_width = 500
can_height = 500
 
# taille d'une case
size = 25
 
# création canevas
can = Canvas(w, width=can_width, height=can_height)
can.pack()
 
def afficher(t):
    """
    Fonction d'affichage du tableau ; 1 élément = 1 case
    La couleur de la "case" dépend de l'état de l'élement correspondant, 0 ou 1
    """
    for i in range(len(t)):
        for j in range(len(t)):
           can.create_rectangle(i * size, j * size , i * size + size, j * size + size, fill = couleurs[tableau[i][j]])
 
def modifierTableau(evt):

    pos_x = int(evt.x / size)
    pos_y = int(evt.y / size)
 
    # inverser la valeur de l'élément cliqué
    if tableau[pos_x][pos_y] == 0:
        tableau[pos_x][pos_y] = 1
    else:
        tableau[pos_x][pos_y] = 0

    # ré-afficher le tableau
    afficher(tableau)
 
#-----------------------------------------------------
# programme
afficher(tableau)
# binding de la fonction modifierTableau sur le canevas
can.bind("<Button-1>", modifierTableau)
# boucle principale
w.mainloop()

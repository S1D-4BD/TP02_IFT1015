# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

import time
#####     INITALISATION DU RANDOM  #####
def rnd():
    s=int(time.time())
    random=(s%6)
    return random

"""
Jai des problèmes avec la librairie random, je vais la simuler avec la librairie time
"""
#####     INITALISATION DE LA PAGE ET JEU  #####

bmb=0  #nombre de jeton
mode=0  #mode de jeu initial (placer les bombes)


def init():         #Fonction servant a initialiser le jeu (la grille, le nombre de bombes, le nbr de cases etc...)
    global bmb
    global rest
    global grille
    global casCont
    global nbrB
    main = document.querySelector("#main")

    nbrB=15 + rnd() #le nombre de bombes initialisé est entre 15 et 20
    bmb=0           #avant de les placer, nous avons initialement 0 bombes placées
    rest=nbrB       
    
    #alert(str(nbrB))
    main.innerHTML = ("""
        <div class="start">
        <button class="hcentered" id="boutonNouvellePartie" onclick="init()">Nouvelle partie</button>
        <button class="hcentered" id="calculer" onclick="calculer()">Calculer</button>
        <button class="hcentered" id="play" onclick="jouer()">jouer</button>
        </div>
        <div class="header_game">
            <div class="msg_jetons">
                <p id="test">Jetons restants:</p>
            </div>
            <div class="msg_erreur">
                <p id="test2">Erreurs: </p>
            </div>
    
        <div id="jeu" class="centered">   
        """ +  genererGrille() + """ 
        </div>
        """)                        #creation de la page HTML (pour la div ayant l'id #main)

    grille = [0] * 100              #initalisation de l'array grille
    casCont = [''] * 100            #initialisation de l'array du contenu des cases
    
    caseC = document.querySelector('#msg')
    caseC.innerHTML =str(casCont)
    #affichage
    gri = document.querySelector('#' + 'grille')
    gri.innerHTML = 'var grille: ' + str(grille.copy())

    for i in range(100): # Nettoyage du grille
        case(i).innerHTML = ''
    



#####     INITALISATION DE LA GRILLE  #####

def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'
def td(contenu): return '<td id="case' + str(contenu) + '" onclick="clic(' + str(contenu) + ')">'+ str(contenu) +'</td>'

"""
on a 3 fct pour générer la grille HTML:
table() crée les balises <table> et appelle tr()
tr() génère une ligne de table() avec les balises <tr>, et appelle td()
td() va crééer la balise <tr> et ajouter un id unique et le onclick correspondant au id
"""

def genererGrille():
    grille = ''
    
    for i in range(0,10):
        temp = ''
        for j in range(0,10):
                index  = i*10+j
                temp += td(index)
        grille += tr(temp)

    return table(grille)
"""
on va générer une grille 10x10 (itérateur i, 10 rangées)
On va faire une boucle imbriquée avec l'itérateur j (10 colonnes)
pour chaque for de j terminé, on ajoute une tr complete (rangée de 10 colonnes)
et apres avoir itéré tout les i (10 rangées), on termine la table """

#####     INITALISATION DES MECANISMES DE JEU  #####

def clic(index):
    global grille
    global nbrB
    global bmb
    global mode
    
    if mode==2:
        jeuclicked(index)
    if bmb < nbrB:
        bmb+=1
        case(index).innerHTML = '<img src="symboles/coste.svg" width="20" height="20">'
        casCont[index]='B'
        caseC = document.querySelector('#msg')
        caseC.innerHTML =str(casCont)

    if grille[index] == 0:
        grille[index] = 1
    #affichage
    gri = document.querySelector('#' + 'grille')
    gri.innerHTML = 'var grille: ' + str(grille.copy())

"""
Fonction clic qui gère les clics sur les cases ()
si le mode est 2 (on joue a trouver les bombes) on appelle jeuclicked
La fonction ajuste les compteurs et l'état des bombes
on met à jour le contenu HTML des cases pour afficher 
le SVG et marque les cases comme étant cliquees (on a mit une bombe là)
"""
#####      FONCTIONS POUR ACCEDER AUX ELEMENTS (DOM)    #####

def element(id):
    return document.querySelector('#' + id)

def case(index):
    return element('case' + str(index))


"""
ces fonctions servent à acceder au dom et a pouvoir les utiliser apres (modifier le contenu, appeler une fonction de jeu etc)
fonction element récupère un élément HTML  en utilisant son id via queryselector
fonction case retourne dynamiquement l'element d'un id mis en parametre précédé du string `case`
"""

#####      FONCTIONS POUR VERIFIER LES CASES ADJACENTES (GRILLE)    #####
def casetoadd(index):
    if casCont[index]=='B':
        return 1
    else:
        return 0

def CaseValue(index):
    global casCont
    global caseCcasetoadd
    result=''
    col=index % 10
    row=(index//10) 
    
    if row == 0:
        if col == 0:
            result=casetoadd(index+1)+casetoadd(index+10)+casetoadd(index+11)
            case(index).innerHTML = str(result)
            
        elif col == 9 :
            result=casetoadd(index-1)+casetoadd(index+9)+casetoadd(index+10)
            case(index).innerHTML = str(result)
            
        else:
            result=casetoadd(index-1)+casetoadd(index+1)+casetoadd(index+9)+casetoadd(index+10)+casetoadd(index+11)
            case(index).innerHTML = str(result)

    if row == 9:
        if col == 0:
            result=casetoadd(index-10)+casetoadd(index-9)+casetoadd(index+1)
            case(index).innerHTML = str(result)
        elif col == 9 :
            result=casetoadd(index-1)+casetoadd(index-10)+casetoadd(index-11)
            case(index).innerHTML = str(result)
        else:
            result=casetoadd(index-1)+casetoadd(index+1)+casetoadd(index-9)+casetoadd(index-10)+casetoadd(index-11)
            case(index).innerHTML = str(result)

    if (row!=0 and col!=0 and row !=9 and col !=9) :
        result= casetoadd(index-9)+casetoadd(index-10)+casetoadd(index-11)+casetoadd(index-1)+casetoadd(index+1)+casetoadd(index+9)+casetoadd(index+10)+casetoadd(index+11) 
        case(index).innerHTML = str(result)
    
    else:
        if col==0 and row!=0 and row!=9:
            result=casetoadd(index-10)+casetoadd(index-9)+casetoadd(index+1)+casetoadd(index+10)+casetoadd(index+11)
            case(index).innerHTML = str(result)
        if col==9 and row!=0 and row!=9:
            result=casetoadd(index-10)+casetoadd(index-11)+casetoadd(index-1)+casetoadd(index+9)+casetoadd(index+10)
            case(index).innerHTML = str(result)
        
    #showMsg("result "+str(index)+str(result))
    if result==0:
        casCont[index]=''
    else:
        casCont[index]=result

"""
Fonction servent à vérifier les cases directement adjacentes
à une case particulière afin de trouver le nombres de bombes s'y trouvant
dependamment des cas, une case peut avoir 3, 5 ou 9 cases adjacentes
Pour chaque bombe trouvée dans les cases adjacentes, la valeur 
de la case vérifiée est incrémentée
"""

#####      FONCTIONS POUR AFFICHER DES MESSAGES DE VICTOIRE OU DEFAITE    #####
    
def showMsg(dtt):
    global casCont
    caseC = document.querySelector('#test')
    caseC.innerHTML =dtt

def showMsg_fail(dtt):
    global casCont
    caseC = document.querySelector('#test2')
    caseC.innerHTML =dtt

"""
fonctions servant à informer le joueur s'il a gagné ou perdu en modifiant le contenu HTML des
div ayant l id #test et #test2
"""

def calculer():
    global casCont
    
    for i in range(0,100):
        if casCont[i] != "B":
            CaseValue(i)
    for j in range(0,100):
        if casCont[j] == "":
            case(j).innerHTML= ""
        if casCont[j] =="B":
            case(j).innerHTML= '<img hidden="hidden" src="symboles/coste.svg" width="20" height="20">'

    caseC = document.querySelector('#msg')
    caseC.innerHTML =str(casCont)  

"""
fonction servant à reveler les bombes lorsquon est en mode jeu (trouver les bombes)
elle parcourt toutes les cases pour déterminer leur contenu
si une case ne contient pas de bombe ('B'), on appelle `CaseValue` pour calculer sa valeur et elle met à jour le HTML des cases
les cases vides sont laissée vides, tandis que celles qui cachaient une bombe ont en ajout le img du svg (coste)
"""


#####      FONCTIONS POUR JOUEUR/REVELER LES BOMBES CACHÉES    #####
def jouer():
    global mode
    global testCount
    global rest
    mode=2      #mode de jeu (chercher les bombes)
    
    testCount=3

def jeuclicked(index):
    global rest
    global testCount
    global mode
    
    #testCount-=1
    if casCont[index]=='B':

        rest=rest-1
        showMsg("Jetons restants: "+str(rest))
        case(index).innerHTML= '<img  src="symboles/coste.svg" width="20" height="20">'
        casCont[index]='T'
        if rest<1 :
            mode=0
            showMsg('Vous avez gagné !')
            time.sleep(10)
            #alert("vous avez gagneeeee")
            case(index).innerHTML= ""
            init()
    else:
        testCount=testCount-1
        showMsg_fail("Essais :  "+str(testCount))
        if testCount<1 :
            mode=0
            showMsg_fail('Vous avez perdu !')
            #alert("vous avez perdu")
            time.sleep(10)
            case(index).innerHTML= ''
            init()
"""
Si la case contient une bombe ('B'), elle décrémente le compteur `rest`
affiche un message avec le nombre de jetons restantset marque la case co mme trouvee ('T')
si toutes les bombes sont trouves, on affiche la victoire et réinitialise après un délai sleep = 10
si la case ne contient pas de bombe, le compteur `testCount` est décrémenté et un premier message d'échec est affiche
si on rate 3 fois on annonce une défaite et le jeu se réinitialise aussi après un délai
"""

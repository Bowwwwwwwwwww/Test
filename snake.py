import pyxel as px
from collections import deque
import random

# CONSTANTE pour la couleur de fond
BG_COLOR = px.COLOR_BLACK
# CONSTANTE pour la couleur du serpent
SNAKE_COLOR = px.COLOR_WHITE
# CONSTANTE pour la couleur de la nourriture
FOOD_COLOR = px.COLOR_RED
score = 0 
def update():
    
    global snake, dx, dy, food, loose, score

    if loose:
        if px.btnp(px.KEY_SPACE):
            test()
            loose = False
            score = 0
        return 

    # Gestion des événements utilisateur
    if px.btnp(px.KEY_UP) and dy != 1:
        dx = 0
        dy = -1
    elif px.btnp(px.KEY_DOWN) and dy != -1:
        dx = 0
        dy = 1
    elif px.btnp(px.KEY_RIGHT) and dx != -1:
        dx = 1
        dy = 0
    elif px.btnp(px.KEY_LEFT) and dx != 1:
        dx = -1
        dy = 0

    # novelle tete du serpent 
    new_tete = (snake[0][0] + dx, snake[0][1] + dy)

    # Si la tete du serpent est aux extremiter de l'ecran sa fait perdre la partie 
    if (new_tete[0] < 0 or new_tete[0] >= px.width or new_tete[1] < 0 or new_tete[1] >= px.height):
        loose = True
        return  #le jeu est perdu 

    # Pour savoir si la tete est dans le corps du serpent pour perdre la partie 
    if new_tete in snake:
        loose = True
        return

    # Vérifier si le serpent mange de la nourriture
    if new_tete == food:
        # on remet la "pomme"/nourriture a un endroit aleatoire de l'ecran 
        
        score = score+1
        print(score)
        food= (random.randint(0, px.width - 1), random.randint(0, px.height - 1))
    else:
        # on retire pour permettre d'avancer 
        snake.pop()
        score = score+1
        txt = str(score)
        print(txt)
        px.text(5, 5, txt, px.COLOR_WHITE)

    # on ajoute la nouvelle tete a la deque 
    snake.appendleft(new_tete)

def draw():
    global snake, food, loose

    px.cls(BG_COLOR)  # Effacer l'écran

    # Dessiner la nourriture
    px.pset(food[0], food[1], FOOD_COLOR)

    if loose:
        # c'est pour afficher perdue quand le joueur a loose 
        px.text(1, 1, "PERDUE", px.COLOR_RED)
        px.text(1, 20, "ESPACE POUR JOUER", px.COLOR_GREEN)
    else:
        # Dessiner le serpent
        for segment in snake:
            px.pset(segment[0], segment[1], SNAKE_COLOR)


def test():
    global snake, dx, dy, food, loose
    # Coordonnées de départ du serpent (une deque de segments)
    snake = deque([(px.width // 2, px.height // 2)])

    # Direction initiale du serpent
    dx = 1
    dy = 0

    # Coordonnées de départ de la nourriture à une position aléatoire
    food= (random.randint(0, px.width - 1), random.randint(0, px.height - 1))

    loose = False  # Réinitialiser le statut du jeu

def init():
    global snake, dx, dy, food, loose

    px.init(25, 25, fps=10)  # Initialiser un écran de 50x50 pixels à 10 FPS



    test()

    px.run(update, draw)  # Lancer la boucle des fonctions update et draw

init()

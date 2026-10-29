import pygame as pg


NB_cols=30
NB_lin=30

Taille_car=20

Longueur= NB_cols*Taille_car
Largeur=NB_lin*Taille_car

Color1= (255,255,255)
Color2= (0,0,0)

def damier(surface):
    for lin in range(NB_lin):
        for col in range(NB_cols):
            Color = Color1 if (lin+col) % 2 == 0 else Color2
            x=Taille_car*col
            y=Taille_car*lin
            rect = pg.Rect(x, y, Taille_car, Taille_car)
            pg.draw.rect(surface, Color, rect)
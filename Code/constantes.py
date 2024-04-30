import pygame

#Matrices 3x3
matriz= [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

matriz_comprobante= [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]


size = 1020, 714 #Tamaño de la pantalla
size_c = 135, 138 #Tamaño de cada cuadrito
#Cargando imagenes
fondo = pygame.image.load("../numeros/fondo.png")
imagen1 = pygame.image.load ("../numeros/1.png")
imagen2 = pygame.image.load ("../numeros/2.png")
imagen3 = pygame.image.load ("../numeros/3.png")
imagen4 = pygame.image.load ("../numeros/4.png")
imagen5 = pygame.image.load ("../numeros/5.png")
imagen6 = pygame.image.load ("../numeros/6.png")
imagen7 = pygame.image.load ("../numeros/7.png")
imagen8 = pygame.image.load ("../numeros/8.png")
i_orange = pygame.image.load ("../numeros/orange.png")
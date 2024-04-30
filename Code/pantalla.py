import pygame
import random
from constantes import *
import sys
from cuadritos import *


pygame.init()

#Cargando sonido de fondo
pygame.mixer.init()
pygame.mixer.music.load("../numeros/Naruto.MP3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)

#Ventana del juego
screen = pygame.display.set_mode((size))
screen_rect = fondo.get_rect()

#Titulo de la ventana
pygame.display.set_caption("SLIDING PUZZLE")

#Instanciando la clase matriz y usando su atributo
mostrar = Matriz()
mostrar.llenar_matriz()
#Instanciando la clase cuadro
mover = Cuadro()

def main():

    #Desordenando la matriz
    random.shuffle(matriz)
    for i in matriz:
        random.shuffle(i)

    #Bandera par mirar si gano o si se sigue ejecutando el juego    
    jugando = True
    # Bucle principal
    while True:
    # Manejo de eventos
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if jugando:
            screen.blit (fondo, screen_rect)
            mostrar.dibujar_matriz() 
            mover.movimiento()

            if matriz_comprobante == matriz:
                #Mensaje para cuando gane 
                fuente = pygame.font.Font(None, 90)
                texto = fuente.render("FELICIDADES"  , 1, (0, 0, 0))
                screen.blit(texto, (305, 10))  
                texto2 = fuente.render("GANASTE"  , 1, (0, 0, 0))
                screen.blit(texto2, (350, 70))
                mostrar.dibujar_matriz()
                jugando = False

            # Actualizar la pantalla
            pygame.display.flip()

main()
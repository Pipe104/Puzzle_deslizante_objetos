import pygame
import random
from constantes import *
import sys
from cuadritos import *
pygame.init()

screen = pygame.display.set_mode((size))
screen_rect = fondo.get_rect()
pygame.display.set_caption("SLIDING PUZZLE")
mostrar = Matriz()
mostrar.llenar_matriz()
mover = Cuadro()

def main():
    random.shuffle(matriz)
    for i in matriz:
        random.shuffle(i)
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
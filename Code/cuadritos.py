import pygame
from constantes import *

screen = pygame.display.set_mode((size))
pygame.init()

class Cuadrado:

    def hacer_imagen(self, imagen):
        self.image = imagen

    def movimiento():
        pass

#Instanciando la clase cuadro para las imagenes
image1 = Cuadrado()
image1.hacer_imagen(imagen1)

image2 = Cuadrado()
image2.hacer_imagen(imagen2)

image3 = Cuadrado()
image3.hacer_imagen(imagen3)

image4 = Cuadrado()
image4.hacer_imagen(imagen4)

image5 = Cuadrado()
image5.hacer_imagen(imagen5)

image6 = Cuadrado()
image6.hacer_imagen(imagen6)

image7 = Cuadrado()
image7.hacer_imagen(imagen7)

image8 = Cuadrado()
image8.hacer_imagen(imagen8)

naranja = Cuadrado()
naranja.hacer_imagen(i_orange)


class Matriz ():

    def __init__ (self):
        self.size_c = size_c #tamaño de cada cuadro 

    def llenar_matriz(self):
        #Llenar la matriz que va a cambiar
        matriz[0][0] = image1
        matriz[0][1] = image2
        matriz[0][2] = image3
        matriz[1][0] = image4
        matriz[1][1] = image5
        matriz[1][2] = image6
        matriz[2][0] = image7
        matriz[2][1] = image8
        matriz[2][2] = naranja

        #Llenar la matriz para comprobar si gano
        matriz_comprobante[0][0] = image1
        matriz_comprobante[0][1] = image2
        matriz_comprobante[0][2] = image3
        matriz_comprobante[1][0] = image4
        matriz_comprobante[1][1] = image5
        matriz_comprobante[1][2] = image6
        matriz_comprobante[2][0] = image7
        matriz_comprobante[2][1] = image8
        matriz_comprobante[2][2] = naranja

    def dibujar_matriz(self):
        #Calcula donde se va a mostrar la matriz (se muestra en el medio)
        start_x = (size[0] - (len(matriz[0]) * self.size_c[0])) // 2
        start_y = (size[1] - (len(matriz) * self.size_c[1])) // 2

        #Mostrando matriz en pantalla
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                screen.blit(matriz[i][j].image, (start_x + j * self.size_c[0], start_y + i * self.size_c[1]))

class Cuadro(Cuadrado):
    
    def __init__ (self):
        #Banderas para que solo detecte un click cuando se toca la tecla
        self.t_p_r = False
        self.t_p_l = False
        self.t_p_u = False
        self.t_p_d = False

    def movimiento(self):
        #Metodo para captar las teclas pulsadas y hacer el movimiento 
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT] and not self.t_p_r:  # Verifica si la tecla está presionada y la bandera es False
            self.t_p_r = True  # Establece la bandera a True
            for i in range(len(matriz)):
                for j in range (len(matriz[i])):
                    if matriz[i][j] == naranja and j != 0:
                        cambio = matriz[i][j-1]
                        matriz[i][j] = cambio
                        matriz [i][j-1] = naranja
        
        if not key[pygame.K_RIGHT]:  # Si la tecla no está presionada, restablece la bandera a False
            self.t_p_r = False
        
        if key[pygame.K_LEFT] and not self.t_p_l:
            self.t_p_l = True
            for i in range(len(matriz)):
                for j in range (len(matriz[i])):
                    if matriz[i][j] == naranja and j != 2:
                        cambio = matriz[i][j+1]
                        matriz[i][j] = cambio
                        matriz [i][j+1] = naranja
                        comprobar = True
                        if comprobar == True:
                            return comprobar
        
        if not key[pygame.K_LEFT]:  # Si la tecla izquierda no está presionada, restablece la bandera a False
            self.t_p_l = False

        if key[pygame.K_DOWN] and not self.t_p_d:
            self.t_p_d = True
            for i in range(len(matriz)):
                for j in range (len(matriz[i])):
                    if matriz[i][j] == naranja and i != 0:
                        cambio = matriz[i-1][j]
                        matriz[i][j] = cambio
                        matriz [i-1][j] = naranja

        
        if not key[pygame.K_DOWN]:  # Si la tecla izquierda no está presionada, restablece la bandera a False
            self.t_p_d = False
        
        if key[pygame.K_UP] and not self.t_p_u:
            self.t_p_u = True
            for i in range(len(matriz)):
                for j in range (len(matriz[i])):
                    if matriz[i][j] == naranja and i != 2:
                        cambio = matriz[i+1][j]
                        matriz[i][j] = cambio
                        matriz [i+1][j] = naranja
                        comprobar = True
                        if comprobar == True:
                            return comprobar
        
        if not key[pygame.K_UP]:  # Si la tecla izquierda no está presionada, restablece la bandera a False
            self.t_p_u = False
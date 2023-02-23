import pygame
import time



pygame.init()

color_uno = (255,255,255)
color_dos = (255,255,102)
color_tres = (0,0,0)
color_cuatro = (213, 200, 80)
color_cinco = (0, 255, 0)
color_seis = (255,0,0)


caja_x = 900
caja_y = 600

captura = pygame.display.set_mode((caja_x, caja_y))
pygame.display.set_caption('SNAKE GAME')

timer = pygame.time.Clock()

culebrita = 10
culebrita_s = 10

display_style = pygame.font.SysFont('arial',30,'bold')
puntos = pygame.font.SysFont('arial',40,'bold')

def puntos_total(puntos):
    value = puntos.reder('este es una prueba de texto')
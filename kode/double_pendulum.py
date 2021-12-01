

import draw_doublependulum
import getopt
import os
import pygame
import numpy
import sys
import math
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

def main():

    # start værdierne på simulationen
    g = 9.82
    dt = 0.01
    m1 = 1.0
    m2 = 1.0
    t1 = math.pi
    t2 = math.pi -0.1
    w1 = 0.0
    w2 = 0.0
    L1 = 1.0
    L2 = 1.0

    # window størrelsen
    Nx = Ny = 500
    # bare en bool til at starte simulationen
    lagrangian = True

    # initialiser dobbeltpendulet
    if lagrangian == True:
        from lagrangian import DoublePendulum
        S = DoublePendulum(g, m1, m2, t1, t2, w1, w2, L1, L2)


 



    # Timer og window simulationen er i
    if lagrangian == True:
        pygame.init()
        clock = pygame.time.Clock()
        window = pygame.display.set_mode((Nx, Ny), pygame.RESIZABLE)
        pygame.display.set_caption("Dobbeltpendul")

    # et evigt while loop til at køre simulationen til man lukker vinduet

    while True:
        # tegne funktionen der køre 60 fps
        if lagrangian == True:
            draw_doublependulum.draw(S, window, Nx, Ny, dt)
         
            clock.tick(60)

            # et forloop der tjekker om man lukker vinduet
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

        # træd dt hen ad x aksen
        S.time_step(dt)
        #addere step med 1
    

        #køre main functionen
if __name__ == "__main__":
    main()



"""tegne functionen til pendulet."""

import math
import numpy
import pygame

def draw(S, window, Nx, Ny, dt):
    """
    Tegner dobbeltpendulet i et vindue

    S - pendul objektet
    window - pop op vinduet
    Nx - størrelsen på vinduet (x-aksen)
    Ny - størrelsen på vinduet (y-aksen)
    dt - hvor meget simulationen træder frem per iteration.
    """

    m1 = S.m1
    m2 = S.m2
    t1 = S.t1
    t2 = S.t2
    L1 = S.L1
    L2 = S.L2

    # størrelsen af kuglerne
    R1 = 10
    R2 = 10

    # Længden på stængerne i pixels
    P1 = 0.85 * min(Nx / 2, Ny / 2) * (L1 / (L1 + L2))
    P2 = 0.85 * min(Nx / 2, Ny / 2) * (L2 / (L1 + L2))

    # Positionen af kuglerne i pixels på simulationen
    X0 = numpy.array([int(Nx / 2), int(Ny / 2)])
    X1 = X0 + numpy.array([int(P1 * math.sin(t1)), int(P1 * math.cos(t1))])
    X2 = X1 + numpy.array([int(P2 * math.sin(t2)), int(P2 * math.cos(t2))])

    # farver ✨æstetik✨
    color_L1 = (255, 255, 255)
    color_L2 = (0, 255, 255)
    color_m1 = (255, 0, 0)
    color_m2 = (0, 0, 255)

    # Baggrund
    window.fill((0, 0, 0))

    # tegner stængerne og kuglerne
    pygame.draw.line(window, color_L1, X0, X1, 4)
    pygame.draw.line(window, color_L2, X1, X2, 4)
    pygame.draw.circle(window, color_m1, X1, int(R1))
    pygame.draw.circle(window, color_m2, X2, int(R2))

    # udskriver vinkelhastighed for begge kugler og tidsinskræmentet
    myfont = pygame.font.SysFont("Arial", 15)
    text1 = myfont.render("dt = %.3g" % dt, 1, (255, 255, 255))
    text2 = myfont.render("Vinkelhastighed kugle 1 = %.3g" % S.w1, 1, (255, 255, 255))
    text3 = myfont.render("Vinkelhastighed kugle 2 = %.3g" % S.w2, 1, (255, 255, 255))


    window.blit(text1, (10, 10))
    window.blit(text2, (10, 30))
    window.blit(text3, (10, 50))

    # refresher billedet
    pygame.display.flip()

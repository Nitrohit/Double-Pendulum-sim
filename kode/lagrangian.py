import os
import math
import numpy
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
class DoublePendulum:

    def __init__(self, g, m1, m2, t1, t2, w1, w2, L1, L2):

        self.g = g
        self.m1 = m1
        self.m2 = m2
        self.t1 = t1
        self.t2 = t2
        self.w1 = w1
        self.w2 = w2
        self.L1 = L1
        self.L2 = L2

    def potential_energy(self):
        """Udregner den potentielle energi af systemet"""

        m1 = self.m1
        t1 = self.t1
        L1 = self.L1
        m2 = self.m2
        t2 = self.t2
        L2 = self.L2

        g = self.g

        # udregner højden på hver kugle
        y1 = -L1 * math.cos(t1)
        y2 = y1 - L2 * math.cos(t2)

        return m1 * g * y1 + m2 * g * y2

    def kinetic_energy(self):
        """udregner den kinetiske energi for hele pendulet"""

        m1 = self.m1
        t1 = self.t1
        w1 = self.w1
        L1 = self.L1
        m2 = self.m2
        t2 = self.t2
        w2 = self.w2
        L2 = self.L2

        # kinetiske energi formel for hver kugle
        K1 = 0.5 * m1 * (L1 * w1)**2
        K2 = 0.5 * m2 * ((L1 * w1)**2 + (L2 * w2)**2 +
                         2 * L1 * L2 * w1 * w2 * math.cos(t1 - t2))

        return K1 + K2


    def mechanical_energy(self):
        """
        udregner den mekaniske energi for hele pendulet
        """

        return self.kinetic_energy() + self.potential_energy()



    def lagrange(self, t1, t2, w1, w2):
        """

        udregner euler-lagrange formlerne for dobbeltpendulet og returnere det som et array

        t1 - vinklen på kugle 1
        t2 - vinklen for kugle 2
        w1 - vinkelhastigheden for kugle 1
        w2 - vinkelhastigheden for kugle 2
        """

        m1 = self.m1
        L1 = self.L1
        m2 = self.m2
        L2 = self.L2

        g = self.g

        a1 = (L2 / L1) * (m2 / (m1 + m2)) * math.cos(t1 - t2)
        a2 = (L1 / L2) * math.cos(t1 - t2)

        f1 = -(L2 / L1) * (m2 / (m1 + m2)) * (w2**2) * math.sin(t1 - t2) - \
            (g / L1) * math.sin(t1)
        f2 = (L1 / L2) * (w1**2) * math.sin(t1 - t2) - (g / L2) * math.sin(t2)

        g1 = (f1 - a1 * f2) / (1 - a1 * a2)
        g2 = (f2 - a2 * f1) / (1 - a1 * a2)

        # her har vi så et arrayet
        return numpy.array([w1, w2, g1, g2])

    def time_step(self, dt):
        """
        her udnytter jeg mig så af den klassiske runge kutte 4 ordens metode
        """

        m1 = self.m1
        t1 = self.t1
        w1 = self.w1
        L1 = self.L1
        m2 = self.m2
        t2 = self.t2
        w2 = self.w2
        L2 = self.L2







        # y er en array med alle koordinaterne (vinkler & vinkelhastighederne)
        y = numpy.array([t1, t2, w1, w2])

        # Runge Kutta 4 ordens metode
        k1 = self.lagrange(*y)
        k2 = self.lagrange(*(y + dt * k1 / 2))
        k3 = self.lagrange(*(y + dt * k2 / 2))
        k4 = self.lagrange(*(y + dt * k3))

        # Udregner 4 orden af runge kutta
        R = 1.0 / 6.0 * dt * (k1 + 2.0 * k2 + 2.0 * k3 + k4)

        # opdatere de nye værdier for vinklerne og vinkelhastigheden
        self.t1 += R[0]
        self.t2 += R[1]
        self.w1 += R[2]
        self.w2 += R[3]

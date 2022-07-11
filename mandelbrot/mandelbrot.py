# Requires the Python mode for Processing.
import time
import math


def complexToPoint(c):
    c += complex(2, 2)
    return (c.imag * float(width + 10) / float(4), c.real * float(1000) / float(4))


def pointToComplex(n):
    x, y = n
    return complex(float(x) * float(4) / (width + 10), float(y) * float(4) / 1000) - complex(2, 2)


class Nokta:
    def __init__(self, n):
        self.x, self.y = n
        self.n = n
        self.complex = pointToComplex(n)
        self.initialComplex = self.complex
        self.dead = False

    def iterate(self):
        self.complex = self.complex**2 + self.initialComplex
        ret = self.complex.imag**2 + self.complex.real**2 <= (2.0)**2
        if not ret:
            self.dead = True
        return ret

    def drawIfDead(self):
        if not self.iterate():
            point(self.x, self.y)
            return False
        return True


kume = []
tekrar = 0
colors = [(0xff, 0x8a, 0x65), (0xff, 0x57, 0x22),
          (0xe6, 0x4a, 0x19), (0xbf, 0x36, 0x0c)]


def setup():
    size(1000, 1000)
    fill(0, 0, 0)
    stroke(0, 0, 0)
    clear()
    for x in range(1000):
        for y in range(1000):
            kume.append(Nokta((x, y)))


lastTimeEliminated = 0
lastTimeDrawn = 0


def draw():
    global kume
    global tekrar
    global lastTimeEliminated
    lastTimeDrawn = time.time()
    tekrar += 1
    numDeleted = 0
    r, g, b = colors[tekrar % len(colors)]
    fill(r, g, b)
    stroke(r, g, b)
    for n in kume:
        if not n.dead:
            if not n.drawIfDead():
                numDeleted += 1
                lastTimeEliminated = tekrar

# Sorry about some non-english variables. I believe that this work is a work of art, I named it as I felt


Height = 900
Width = 900
tekrar = 100


class Bubble(object):
    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_
        self.r = random(5, 150)
        self.r_change()

    def show(self):

        circle(self.x, self.y, self.r*2)

    def getlist(self):
        a = [self.x, self.y, self.r]
        return a

    def r_change(self):
        if dist(self.x, self.y, 450, 450) + self.r > 300:
            self.x = random(0, 900)
            self.y = random(0, 900)
            self.r = random(5, 25)
            self.r_change()


liste = []
startbubble = Bubble(random(200, 700), random(200, 700))
startbubble2 = Bubble(random(200, 700), random(200, 700))
startbubble.r = 50
startbubble2.r = 50
liste.append(startbubble)
liste.append(startbubble2)


def newCircle():
    global liste
    new = Bubble(random(0, 900), random(0, 900))

    puan = 0
    for i in liste:
        rtotal = new.r + i.r
        merkez = dist(i.x, i.y, new.x, new.y)
        if(rtotal < merkez):
            puan += 1
    if puan == len(liste):
        liste.append(new)
        return new.show()
    return newCircle()

    liste.append(new)
    return new.show()


def setup():
    global Height, Width
    size(Width, Height)
    bg = color(255, 255, 255)
    background(bg)


def draw():
    noFill()
    # circle(450,450,600)
    if len(liste) < 300:
        fill(random(0, 255), random(0, 255), random(0, 255))
        newCircle()
    else:
        noLoop()

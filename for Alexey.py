import pygame
from pygame.draw import *


pygame.init()
FPS=30

#create screen and surfaces
screen = pygame.display.set_mode((927,769))
surface = pygame.Surface((927,769), pygame.SRCALPHA)

#create body of man
circle(screen, (255,102,0), (464,769), 225)

#create hands
ellipse(screen, (234,199,176), rect(surface, (0,0,0), (45,40,70,90)))
ellipse(screen, (234,199,176), rect(surface, (0,0,0), (805,40,70,90)))
line(screen, (234,199,176), (75,105), (215,560), 30)
line(screen, (234,194,176), (845,105), (705,560), 30)

#create rectangle for letters
rect(screen, (50,255,50), (0,0,927,82))

#create T-shirt
x=82
y=220
polygon(screen, (250,102,0), [(96+x,356+y), (172+x,316+y), (229+x,382+y), (187+x,469+y), (102+x,459+y)])
polygon(screen, (0,0,0), [(96+x,356+y), (172+x,316+y), (229+x,382+y), (187+x,469+y), (102+x,459+y)], 1)
x=520
y=220
polygon(screen, (250,102,0), [(225+x,355+y), (150+x,310+y), (87+x,368+y), (120+x,459+y), (210+x,448+y)])
polygon(screen, (0,0,0), [(225+x,355+y), (150+x,310+y), (87+x,368+y), (120+x,459+y), (210+x,448+y)], 1)

# create head
circle(screen, (234,199,176), (464,410), 225)
#eyes
circle(screen, (127,177,255), (394,380), 40)
circle(screen, (4, 0, 5), (394,380), 10)
circle(screen, (127,177,255), (534,380), 40)
circle(screen, (4, 0, 5), (534,380), 10)
#nose
polygon(screen, (103,58,25), [(448,420), (464,445), (480,420)])
#mouth
polygon(screen, (233,37,40), [(344,475), (464,550), (584,475)])
#hair
PURPLE = (212,42,254)
RED = (255, 0, 0)
YELLOW = (255, 254, 0)
PINK = (255, 59, 125)
BLUE = (12, 35, 255)
polygon(screen, PURPLE, [(250,250), (310,245), (270,300)])
polygon(screen, PURPLE, [(303,257), (308,189), (349,215)])
polygon(screen, PURPLE, [(341,223), (344,173), (390,198)])
polygon(screen, PURPLE, [(384,197), (408,150), (434,186)])
polygon(screen, PURPLE, [(419,188), (442,144), (462,181)])
polygon(screen, PURPLE, [(451,183), (480,150), (488,181)])
polygon(screen, PURPLE, [(484,182), (530,150), (535,194)])
polygon(screen, PURPLE, [(535,194), (590,171), (590,220)])
polygon(screen, PURPLE, [(577,215), (640,200), (621,245)])
polygon(screen, PURPLE, [(609,232), (671,220), (645,270)])




#p
line(screen, (0,0,0), (36,59), (36,18), 10)
circle(screen, (0,0,0), (45,28), 15)
circle(screen, (50,255,50), (45,28), 8)
#y
line(screen, (0,0,0), (86,59), (86,38), 10)
line(screen, (0,0,0), (86,38), (66,18), 10)
line(screen, (0,0,0), (86,38), (106,18), 10)
#t
line(screen, (0,0,0), (136,59), (136,18), 10)
line(screen, (0,0,0), (116,18), (156,18), 10)
#h
line(screen, (0,0,0), (176,59), (176,18), 10)
line(screen, (0,0,0), (196,59), (196,18), 10)
line(screen, (0,0,0), (176,38), (196,38), 10)
#0
circle(screen, (0,0,0), (236,38), 25)
circle(screen, (50,255,50), (236,38), 19)
#n
line(screen, (0,0,0), (276,59), (276,18), 10)
line(screen, (0,0,0), (296,59), (296,18), 10)
line(screen, (0,0,0), (276,18), (296,59), 10)



#i
line(screen, (0,0,0), (366,59), (366,28), 10)
line(screen, (0,0,0), (366,22), (366,18), 10)
#z
line(screen, (0,0,0), (386,18), (426,18), 10)
line(screen, (0,0,0), (386,59), (426,59), 10)
line(screen, (0,0,0), (386,18), (426,59), 10)


delta = 20
#a
line(screen, (0,0,0), (446+delta,59), (466+delta,18), 10)
line(screen, (0,0,0), (486+delta,59), (466+delta,18), 10)
line(screen, (0,0,0), (456+delta,46), (476+delta,46), 10)
#m
line(screen, (0,0,0), (496+delta,59), (496+delta,18), 10)
line(screen, (0,0,0), (536+delta,59), (536+delta,18), 10)
line(screen, (0,0,0), (516+delta,46), (496+delta,18), 10)
line(screen, (0,0,0), (516+delta,46), (536+delta,18), 10)
#a
line(screen, (0,0,0), (546+delta,59), (566+delta,18), 10)
line(screen, (0,0,0), (586+delta,59), (566+delta,18), 10)
line(screen, (0,0,0), (556+delta,46), (576+delta,46), 10)
#z
line(screen, (0,0,0), (606+delta,18), (646+delta,18), 10)
line(screen, (0,0,0), (606+delta,59), (646+delta,59), 10)
line(screen, (0,0,0), (606+delta,59), (646+delta,18), 10)
#i
line(screen, (0,0,0), (656+delta,59), (656+delta,28), 10)
line(screen, (0,0,0), (656+delta,22), (656+delta,18), 10)
#n
line(screen, (0,0,0), (676+delta,59), (676+delta,18), 10)
line(screen, (0,0,0), (696+delta,59), (696+delta,18), 10)
line(screen, (0,0,0), (676+delta,18), (696+delta,59), 10)
#g
circle(screen, (0,0,0), (736+delta,38), 25)
circle(screen, (50,255,50), (736+delta,38), 19)
rect(screen, (50,255,50), (746+delta,5,40,40))
line(screen, (0,0,0), (736+delta,42), (761+delta,42), 6)

def smail(start_x, start_y, color):
    screen1 = pygame.Surface((927,769))
    screen1.set_colorkey((0, 0, 0))
    # create head
    circle(screen1, (234,199,176), (464,410), 225)
    #eyes
    circle(screen1, (127,177,255), (394,380), 40)
    circle(screen1, (4, 0, 5), (394,380), 10)
    circle(screen1, (127,177,255), (534,380), 40)
    circle(screen1, (4, 0, 5), (534,380), 10)
    #nose
    polygon(screen1, (103,58,25), [(448,420), (464,445), (480,420)])
    #mouth
    polygon(screen1, (233,37,40), [(344,475), (464,550), (584,475)])
    # hair
    polygon(screen1, color, [(250, 250), (310, 245), (270, 300)])
    polygon(screen1, color, [(303, 257), (308, 189), (349, 215)])
    polygon(screen1, color, [(341, 223), (344, 173), (390, 198)])
    polygon(screen1, color, [(384, 197), (408, 150), (434, 186)])
    polygon(screen1, color, [(419, 188), (442, 144), (462, 181)])
    polygon(screen1, color, [(451, 183), (480, 150), (488, 181)])
    polygon(screen1, color, [(484, 182), (530, 150), (535, 194)])
    polygon(screen1, color, [(535, 194), (590, 171), (590, 220)])
    polygon(screen1, color, [(577, 215), (640, 200), (621, 245)])
    polygon(screen1, color, [(609, 232), (671, 220), (645, 270)])
    screen1 = pygame.transform.scale(screen1, (309, 256))
    screen.blit(screen1, (start_x, start_y))


smail(50, 50, RED)
smail(550, 50, YELLOW)
smail(0, 350, PINK)
smail(600, 350, BLUE)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

from pygame import *

sc_width = 700
sc_height = 500
scene = display.set_mode(sc_width, sc_height)




clock = time.Clock()
FPS = 60

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            
window.fill(214, 174, 211)

display.update()
clock.tick(FPS)
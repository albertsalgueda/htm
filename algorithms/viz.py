import numpy as np
from PIL import Image
import pygame

#WORK IN PROGRESS

def grid(window,size,rows):
    distance = size//rows
    x = 0
    y = 0
    for i in range(rows):
        x += distance
        y += distance 
        pygame.draw.line(window, (0,0,0), (x,0), (x,size))
        pygame.draw.line(window, (0,0,0), (0,y), (size,y))
    win =  pygame.display.set_mode((int(distance),int(distance)))
    cube(win)

def cube(win):
    win.fill((255,255,255))

def redraw(window):
    global size,rows
    window.fill((255, 255,255))
    grid(window,size,rows)
    pygame.display.update()


def main():
    global size,rows
    size = 500
    rows = 20

    window = pygame.display.set_mode((size,size))
    play = True

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        redraw(window)


main()


"""
w, h = 1000, 1000
data = np.zeros((h, w, 3), dtype=np.uint8)
data[0:int(w/2), 0:int(h/2)] = [255, 0, 0] # red patch in upper left
print(data)
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()
"""
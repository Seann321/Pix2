import pygame
from random import randint


pygame.init()

# Screen size
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height))

# RGB Background color
backgroundColor = (100, 100, 100)
screen.fill(backgroundColor)

# Title
pygame.display.set_caption('Pix')

# Update whole display using flip
pygame.display.flip()


class Pix:
    def __init__(self, color, location):
        self.Color = color
        self.Location = pygame.Rect(location)
        self.Locked = False


running = True

# Time Vars
FPS = 1000
clock = pygame.time.Clock()
deltaTime = clock.tick(FPS)


# Pix Array
pixArrays = []
pixSize = int(width/100)

for i in range(int(width/pixSize)):
    pixArrays.append([])


while running:
    clock.tick(FPS)
    # Loop through event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
    if randint(1, 7) == 1:
        xValue = randint(0, int(width/pixSize)-1)
        pixArrays[xValue].append((Pix([randint(1, 255), randint(1, 255), randint(1, 255)], [xValue * pixSize, -pixSize, pixSize, pixSize])))
    for arrayColumn in range(len(pixArrays)):
        for i in range(len(pixArrays[arrayColumn])):
            if pixArrays[arrayColumn][i].Locked:
                continue
            for x in range(len(pixArrays[arrayColumn])):
                if not pixArrays[arrayColumn][x].Locked:
                    continue
                if pixArrays[arrayColumn][x].Location[0] != pixArrays[arrayColumn][i].Location[0]:
                    continue
                if pixArrays[arrayColumn][i].Location.colliderect(pixArrays[arrayColumn][x].Location):
                    pixArrays[arrayColumn][i].Locked = True
            if pixArrays[arrayColumn][i].Location[1] < height - pixSize + 1:
                pixArrays[arrayColumn][i].Location[1] += 1
                pygame.draw.rect(screen, pixArrays[arrayColumn][i].Color, pixArrays[arrayColumn][i].Location)
                pygame.display.update(pixArrays[arrayColumn][i].Location)
            else:
                pixArrays[arrayColumn][i].Locked = True

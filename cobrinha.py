import pygame
from pygame.locals import *
import random

windowSize = (600, 600)
pixelSize = 10


def colision(pos1, pos2):
    return pos1 == pos2


def off_limits(pos):
    if 0 <= pos[0] < windowSize[0] and 0 <= pos[1] < windowSize[1]:
        return False
    else:
        return True


def randomOnGrid():
    x = random.randint(0, windowSize[0])
    y = random.randint(0, windowSize[1])
    return x // pixelSize * pixelSize, y // pixelSize * pixelSize


def restartGame():
    global snake_pos
    global apple_pos
    global snakeDirection
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snakeDirection = K_LEFT
    apple_pos = randomOnGrid()


pygame.init()
screen = pygame.display.set_mode((windowSize))
pygame.display.set_caption('Snake')

"""Variáveis da cobrinha: """
snake_pos = [(250, 50), (260, 50), (270, 50)]
snakeSurface = pygame.Surface((pixelSize, pixelSize))
snakeSurface.fill((255, 255, 255))
snakeDirection = K_LEFT
"""Fim das variáveis da cobrinha: """


"""Variáveis da maçã: """
appleSurface = pygame.Surface((pixelSize, pixelSize))
appleSurface.fill((255, 0, 0))
apple_pos = randomOnGrid()
"""Fim das variáveis da maçã: """


while True:
    pygame.time.Clock().tick(15)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            quit()

        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snakeDirection = event.key

    screen.blit(appleSurface, apple_pos)

    if colision(apple_pos, snake_pos[0]):
        snake_pos.append((-10, -10))
        apple_pos = randomOnGrid()

    for pos in snake_pos:
        screen.blit(snakeSurface, pos)

    for i in range(len(snake_pos)-1, 0, -1):
        if colision(snake_pos[0], snake_pos[i]):
            restartGame()
        snake_pos[i] = snake_pos[i - 1]

    if off_limits(snake_pos[0]):
        restartGame()

    if snakeDirection == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - pixelSize)
    elif snakeDirection == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + pixelSize)
    elif snakeDirection == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - pixelSize, snake_pos[0][1])
    elif snakeDirection == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + pixelSize, snake_pos[0][1])

    pygame.display.update()

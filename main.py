#The main file of the program
import pygame
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *

#imports of specific models
from ground_plane import ground
from houses import *


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        ground()
        test_house()

        pygame.display.flip()
        pygame.time.wait(75)

main()
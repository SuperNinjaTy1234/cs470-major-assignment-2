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
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -3) #Must push the camera because it spawns inside the cube

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
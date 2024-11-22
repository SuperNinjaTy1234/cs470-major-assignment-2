# The main file of the program
import pygame
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *

# imports of specific models
from ground_plane import *
from houses import *
from roads import *


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10) #Must push the camera because it spawns inside the cube
    glRotatef(15, 1, 0, 0)

    move_on_x = 0
    move_on_y = 0
    move_on_z = 0
    rotate = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_on_x = 1
                elif event.key == pygame.K_d:
                    move_on_x = -1
                elif event.key == pygame.K_s:
                    move_on_z = -1
                elif event.key == pygame.K_w:
                    move_on_z = 1
                elif event.key == pygame.K_r:
                    rotate = 1
                elif event.key == pygame.K_l:
                    rotate = -1
                elif event.key == pygame.K_UP:
                    move_on_y = -1
                elif event.key == pygame.K_DOWN:
                    move_on_y = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    move_on_x = 0
                elif event.key == pygame.K_d:
                    move_on_x = 0
                elif event.key == pygame.K_s:
                    move_on_z = 0
                elif event.key == pygame.K_w:
                    move_on_z = 0
                elif event.key == pygame.K_r:
                    rotate = 0
                elif event.key == pygame.K_l:
                    rotate = 0
                elif event.key == pygame.K_UP:
                    move_on_y = 0
                elif event.key == pygame.K_DOWN:
                    move_on_y = 0

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        ground()
        draw_road()
        draw_house()


        glTranslatef(move_on_x, move_on_y, move_on_z)

        #For some reason, this makes the camera get farther and farther away
        if rotate == 1 or rotate == -1:
            glRotatef(10, 0, rotate, 0)

        pygame.display.flip()
        pygame.time.wait(75)

main()
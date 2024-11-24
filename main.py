#The main file of the program
import pygame
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *

#imports of specific models
from ground_plane import *
from body_of_water import *
from houses import *
from roads import *
from light import setup_daylight, setup_nightlight
from background import load_texture, draw_background

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)   #Must push the camera because it spawns inside the cube
    glRotatef(15, 1, 0, 0)

    bg_texture = load_texture("Textures/mountain.jpg")  # Load the mountain texture

    setup_daylight()  # Start with daylight

    # Enabled features
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    move_on_x = 0
    move_on_y = 0
    move_on_z = 0
    rotate = 0
    is_daytime = True  # Lighting state

    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -10)

        draw_background(bg_texture)  # Draw the background first

        glTranslatef(move_on_x, move_on_y, move_on_z)
        if rotate:
            glRotatef(10, 0, rotate, 0)

        ground()
        draw_water_plane()
        draw_road()
        test_house()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_on_x = 1
                elif event.key == pygame.K_d:
                    move_on_x = -1
                elif event.key is pygame.K_s:
                    move_on_z = -1
                elif event.key is pygame.K_w:
                    move_on_z = 1
                elif event.key is pygame.K_r:
                    rotate = 1
                elif event.key is pygame.K_l:
                    rotate = -1
                elif event.key is pygame.K_UP:
                    move_on_y = -1
                elif event.key is pygame.K_DOWN:
                    move_on_y = 1
                elif event.key is pygame.K_t:  # Toggle lighting
                    is_daytime = not is_daytime
                    if is_daytime:
                        setup_daylight()
                    else:
                        setup_nightlight()

            if event.type is pygame.KEYUP:
                if event.key in (pygame.K_a, pygame.K_d):
                    move_on_x = 0
                if event.key in (pygame.K_s, pygame.K_w):
                    move_on_z = 0
                if event.key in (pygame.K_r, pygame.K_l):
                    rotate = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    move_on_y = 0

        pygame.display.flip()
        pygame.time.wait(75)

if __name__ == "__main__":
    main()

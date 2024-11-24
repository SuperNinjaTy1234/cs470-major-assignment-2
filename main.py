# The main file of the program
import pygame
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *

# Import lighting setups
from light import setup_daylight, setup_nightlight

# Imports of specific models
from ground_plane import *
from houses import *
from roads import *
from background import load_texture, draw_background

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    bg_texture = load_texture("Textures/mountain.jpg")

    # Start with daylight
    setup_daylight()

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    move_on_x = 0
    move_on_y = 0
    move_on_z = 0
    rotate = 0
    is_daytime = True  # Track lighting state

    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Reset view before drawing background
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)  # Reset the camera each frame
        draw_background(bg_texture)

        # Setup transformations for other objects
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)
        glTranslatef(move_on_x, move_on_y, move_on_z)
        if rotate == 1 or rotate == -1:
            glRotatef(10, 0, rotate, 0)

        ground()
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
                elif event.key == pygame.K_t:  # Toggle day/night with 't'
                    is_daytime = not is_daytime
                    if is_daytime:
                        setup_daylight()
                    else:
                        setup_nightlight()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    move_on_x = 0
                elif event.key == pygame.K_d:
                    move_on_x = 0
                elif event.key == pygame.K_s:
                    move_on_z = 0
                elif event.key is pygame.K_w:
                    move_on_z = 0
                elif event.key == pygame.K_r:
                    rotate = 0
                elif event.key == pygame.K_l:
                    rotate = 0
                elif event.key == pygame.K_UP:
                    move_on_y = 0
                elif event.key is pygame.K_DOWN:
                    move_on_y = 0

        pygame.display.flip()
        pygame.time.wait(75)

if __name__ == "__main__":
    main()

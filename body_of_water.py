# CREDIT:
#
# Link:
# license:
# NOTE: No changes were made to the texture used

import pygame.image
from OpenGL.GL import *

edges = (
    (-10, 0.01, 35),
    (0, 0.01, 35),
    (0, 0.01, -35),
    (-10, 0.01, -35)
)

tex_edges = (
    (0, 0),
    (0, 25),
    (25, 25),
    (25, 0)
)

def draw_water_plane():
    glPushMatrix()
    glTranslatef(-8, 0, 1)
    glRotate(90, 0, 1, 0)
    water_plane()
    glPopMatrix()

def water_plane():
    glBegin(GL_QUADS)

    glColor3f(0, 0, 1)

    for edge in edges:
        glVertex3fv(edge)

    glEnd()
    glFlush()
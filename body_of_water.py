# CREDIT:
# The water texture used in this project was created by Aswin909 (Aswin Vos) on OpenGameArt.org
# Link: https://opengameart.org/content/water
# license: CC-BY-SA 3.0
# NOTE: No changes were made to the texture used, but the file name was changed to "water.jpg"

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
    (0, 1),
    (10, 1),
    (10, 0)
)

def draw_water_plane():
    glPushMatrix()
    glTranslatef(-8, 0, 1)
    glRotate(90, 0, 1, 0)
    water_plane()
    glPopMatrix()

def water_plane():
    #Texture Mapping variables
    glEnable(GL_TEXTURE_2D)
    water_texture = pygame.image.load('Textures/Aswin909/water.jpg')
    water_texture_data = pygame.image.tostring(water_texture, 'RGBA', True)
    water_texture_id = glGenTextures(1)

    #Texture Bindings
    glBindTexture(GL_TEXTURE_2D, water_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, water_texture.get_width(), water_texture.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, water_texture_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glBegin(GL_QUADS)

    glColor3f(1, 1, 1)

    for edge, tex_edge in zip(edges, tex_edges):
        glTexCoord2f(tex_edge[0], tex_edge[1])
        glVertex3fv(edge)

    glEnd()
    glFlush()
# CREDIT:
# The grass texture used in this project was created by Snabisch on OpenGameArt.org
# Link: https://opengameart.org/content/free-tiling-3d-grass-texture
# license: CC-BY 4.0, CC-BY 3.0, OGA-BY 3.0
# NOTE: No changes were made to the texture used

import pygame.image
from OpenGL.GL import *

edges = (
    (-200, 0, 200),
    (200, 0, 200),
    (200, 0, -200),
    (-200, 0, -200)
)

tex_edges = (
    (0, 0),
    (0, 25),
    (25, 25),
    (25, 0)
)

def ground():
    #Texture variables
    glEnable(GL_TEXTURE_2D)
    grass_texture = pygame.image.load('Textures/grassy_d.png')
    grass_texture_data = pygame.image.tostring(grass_texture, 'RGBA', True)
    grass_texture_id = glGenTextures(1)

    #Texture bindings
    glBindTexture(GL_TEXTURE_2D, grass_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, grass_texture.get_width(), grass_texture.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, grass_texture_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)

    #This goes through each tuple - better way to do it
    for edge, tex_edge in zip(edges, tex_edges):
        glTexCoord2f(tex_edge[0], tex_edge[1])
        glVertex3fv(edge)

    glEnd()
    glFlush()
    glDisable(GL_TEXTURE_2D)
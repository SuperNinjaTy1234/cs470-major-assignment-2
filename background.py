import pygame
from OpenGL.GL import *


def load_texture(image_path):
    texture_surface = pygame.image.load(image_path)
    texture_data = pygame.image.tostring(texture_surface, "RGBA", True)
    width = texture_surface.get_width()
    height = texture_surface.get_height()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    glBindTexture(GL_TEXTURE_2D, 0)  # Unbind the texture when done
    return texture_id


def draw_background(texture_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0);
    glVertex3f(-10.0, -10.0, -20.0)
    glTexCoord2f(1, 0);
    glVertex3f(10.0, -10.0, -20.0)
    glTexCoord2f(1, 1);
    glVertex3f(10.0, 10.0, -20.0)
    glTexCoord2f(0, 1);
    glVertex3f(-10.0, 10.0, -20.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)

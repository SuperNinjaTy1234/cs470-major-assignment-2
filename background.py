import pygame
from OpenGL.GL import *
from OpenGL.raw.GLU import gluOrtho2D


def load_texture(image_path):
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    image = pygame.image.load(image_path)
    image_data = pygame.image.tostring(image, "RGBA", 1)
    width, height = image.get_size()
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    return texture


def draw_background(texture):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-100, -100, -40)
    glTexCoord2f(1, 0); glVertex3f(100, -100, -40)
    glTexCoord2f(1, 1); glVertex3f(100, 100, -40)
    glTexCoord2f(0, 1); glVertex3f(-100, 100, -40)
    glEnd()

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(100, -100, -40)
    glTexCoord2f(1, 0); glVertex3f(100, -100, 40)
    glTexCoord2f(1, 1); glVertex3f(100, 100, 40)
    glTexCoord2f(0, 1); glVertex3f(100, 100, -40)
    glEnd()

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-100, -100, 40)
    glTexCoord2f(1, 0); glVertex3f(-100, -100, -40)
    glTexCoord2f(1, 1); glVertex3f(-100, 100, -40)
    glTexCoord2f(0, 1); glVertex3f(-100, 100, 40)
    glEnd()

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-100, 100, -40)
    glTexCoord2f(1, 0); glVertex3f(100, 100, -40)
    glTexCoord2f(1, 1); glVertex3f(100, 100, 40)
    glTexCoord2f(0, 1); glVertex3f(-100, 100, 40)
    glEnd()

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-100, -100, 40)
    glTexCoord2f(1, 0); glVertex3f(100, -100, 40)
    glTexCoord2f(1, 1); glVertex3f(100, 100, 40)
    glTexCoord2f(0, 1); glVertex3f(-100, 100, 40)
    glEnd()

    glDisable(GL_TEXTURE_2D)

def init_opengl(display_size):
    pygame.init()
    pygame.display.set_mode(display_size, pygame.DOUBLEBUF | pygame.OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)  # Set orthographic projection for 2D rendering
    glMatrixMode(GL_MODELVIEW)


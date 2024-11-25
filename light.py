from OpenGL.GL import *

def setup_daylight():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)    # light #0

    # Set up light color (ambient, diffuse, specular)
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 1, 1, 1))

    # Position the light (x, y, z, w)
    # w is 0 for directional light (sun), 1 for point light
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 10, 10, 0.0))

    # Setup global ambient light
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.2, 0.2, 0.2, 1))

def setup_nightlight():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    # Dimmer ambient and diffuse components for night
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.1, 0.1, 0.1, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.3, 0.3, 0.3, 1))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.5, 0.5, 0.5, 1))

    # Reposition the light for night
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 5, 5, 0.0))

    # Change global ambient light to be darker
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.05, 0.05, 0.05, 1))

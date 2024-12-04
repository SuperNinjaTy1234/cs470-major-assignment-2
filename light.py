from OpenGL.GL import *

def light_init(is_daytime):
    #Light 0 Setup
    if is_daytime:
        glLightfv(GL_LIGHT0, GL_POSITION, (0, 10, 10, 0.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
        glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 1, 1, 1))
    else:
        glLightfv(GL_LIGHT0, GL_POSITION, (0, 5, 5, 0.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.1, 0.1, 0.1, 1))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.3, 0.3, 0.3, 1))
        glLightfv(GL_LIGHT0, GL_SPECULAR, (0.5, 0.5, 0.5, 1))

    #Light 1 Setup - Outside light 1
    glLightfv(GL_LIGHT1, GL_POSITION, (-26, 12, 0, 1.0))
    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 25.0)
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, (0.0, -1.0, 0.0, 0.0))
    glLightfv(GL_LIGHT1, GL_AMBIENT, (1, 1, 1, 1))
    glLightfv(GL_LIGHT1, GL_DIFFUSE, (1, 1, 1, 1))
    glLightfv(GL_LIGHT1, GL_SPECULAR, (1, 1, 1, 1))

    # Light 2 Setup - Outside light 2
    glLightfv(GL_LIGHT2, GL_POSITION, (-42, 12, 0, 1.0))
    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 25.0)
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, (0.0, -1.0, 0.0, 0.0))
    glLightfv(GL_LIGHT2, GL_AMBIENT, (1, 1, 1, 1))
    glLightfv(GL_LIGHT2, GL_DIFFUSE, (1, 1, 1, 1))
    glLightfv(GL_LIGHT2, GL_SPECULAR, (1, 1, 1, 1))

    # Light 3 Setup - Orange House light
    glLightfv(GL_LIGHT3, GL_POSITION, (8, 5, -7, 1.0))
    glLightf(GL_LIGHT3, GL_SPOT_CUTOFF, 30.0)
    glLightfv(GL_LIGHT3, GL_SPOT_DIRECTION, (0.0, -1.0, 0.0, 0.0))
    glLightfv(GL_LIGHT3, GL_AMBIENT, (0.5, 0.5, 0.5, 1))
    glLightfv(GL_LIGHT3, GL_DIFFUSE, (1, 1, 1, 1))
    glLightfv(GL_LIGHT3, GL_SPECULAR, (0, 0, 0, 0))

    # Light 4 Setup - Purple House light
    glLightfv(GL_LIGHT4, GL_POSITION, (-7, 8, -8, 1.0))
    glLightf(GL_LIGHT4, GL_SPOT_CUTOFF, 30.0)
    glLightfv(GL_LIGHT4, GL_SPOT_DIRECTION, (0.0, -1.0, 0.0, 0.0))
    glLightfv(GL_LIGHT4, GL_AMBIENT, (0.5, 0.5, 0.5, 1))
    glLightfv(GL_LIGHT4, GL_DIFFUSE, (1, 1, 1, 1))
    glLightfv(GL_LIGHT4, GL_SPECULAR, (0, 0, 0, 0))

    # Light 4 Setup - Red House light
    glLightfv(GL_LIGHT5, GL_POSITION, (-2, 8, -7, 1.0))
    glLightf(GL_LIGHT5, GL_SPOT_CUTOFF, 30.0)
    glLightfv(GL_LIGHT5, GL_SPOT_DIRECTION, (0.0, -1.0, 0.0, 0.0))
    glLightfv(GL_LIGHT5, GL_AMBIENT, (0.5, 0.5, 0.5, 1))
    glLightfv(GL_LIGHT5, GL_DIFFUSE, (1, 1, 1, 1))
    glLightfv(GL_LIGHT5, GL_SPECULAR, (0, 0, 0, 0))

    # Light 4 Setup - Green House light
    glLightfv(GL_LIGHT6, GL_POSITION, (2.7, 8, -7, 1.0))
    glLightf(GL_LIGHT6, GL_SPOT_CUTOFF, 30.0)
    glLightfv(GL_LIGHT6, GL_SPOT_DIRECTION, (0.0, -1.0, 0.0, 0.0))
    glLightfv(GL_LIGHT6, GL_AMBIENT, (0.5, 0.5, 0.5, 1))
    glLightfv(GL_LIGHT6, GL_DIFFUSE, (1, 1, 1, 1))
    glLightfv(GL_LIGHT6, GL_SPECULAR, (0, 0, 0, 0))


def enable_daytime_lighting():
    glEnable(GL_LIGHT0)  # light #0
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.2, 0.2, 0.2, 1))
    glDisable(GL_LIGHT1) #outside light 1
    glDisable(GL_LIGHT2)  #outside light 2
    glDisable(GL_LIGHT3) #inside light 1
    glDisable(GL_LIGHT4) #inside light 2
    glDisable(GL_LIGHT5)  # inside light 3
    glDisable(GL_LIGHT6)  # inside light 4

def enable_nighttime_lighting():
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHT2)
    glEnable(GL_LIGHT3)
    glEnable(GL_LIGHT4)
    glEnable(GL_LIGHT5)
    glEnable(GL_LIGHT6)



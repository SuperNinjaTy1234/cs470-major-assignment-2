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

    #Light 1 Setup
    glLightfv(GL_LIGHT1, GL_POSITION, (-26, 5.4, -3, 1.0))
    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 60.0)
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, (0.0, -1.0, 0.0, 0.0))
    glLightfv(GL_LIGHT1, GL_AMBIENT, (0.1, 0.1, 0.1, 1))
    glLightfv(GL_LIGHT1, GL_DIFFUSE, (1, 1, 1, 1))
    glLightfv(GL_LIGHT1, GL_SPECULAR, (0, 0, 0, 0))

    # Light 2 Setup
    glLightfv(GL_LIGHT2, GL_POSITION, (-41.5, 10.4, -3, 1.0))
    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 60.0)
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, (0.0, -1.0, 0.0, 0.0))
    glLightfv(GL_LIGHT2, GL_AMBIENT, (0.1, 0.1, 0.1, 1))
    glLightfv(GL_LIGHT2, GL_DIFFUSE, (1, 1, 1, 1))
    glLightfv(GL_LIGHT2, GL_SPECULAR, (0, 0, 0, 0))


def enable_daytime_lighting():
    glEnable(GL_LIGHT0)  # light #0
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.2, 0.2, 0.2, 1))
    glDisable(GL_LIGHT1) #outside light 1
    glDisable(GL_LIGHT2)  #outside light 2

def enable_nighttime_lighting():
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHT2)



from OpenGL.GL import *

def enable_daytime_lighting():
    setup_daylight()
    glDisable(GL_LIGHT1) #outside light 1
    glDisable(GL_LIGHT2)  #outside light 2

def enable_nighttime_lighting():
    setup_nightlight()
    setup_outside_lights()
    #setup_house_light1()

def setup_daylight():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)    # light #0

    # Set up light color (ambient, diffuse, specular)
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 1, 1, 1))

    # Position the light (x, y, z, w)
    # w is 1 for directional light (sun), 1 for point light
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

def setup_outside_lights():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHT2)

    ambient = (0.1, 0.1, 0.1, 1)
    diffuse = (1, 1, 1, 1)
    specular = (0, 0, 0, 0)

    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 60.0)
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, (0.0, -1.0, 0.0, 0.0))

    glLightfv(GL_LIGHT1, GL_AMBIENT, ambient)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT1, GL_SPECULAR, specular)

    # Position the light (x, y, z, w)
    # w is 0 for directional light (sun), 1 for point light
    #glLightfv(GL_LIGHT1, GL_POSITION, (0, 5.4, 0, 1.0))

    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 45.0)
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, (0.0, -1.0, 0.0, 0.0))

    glLightfv(GL_LIGHT2, GL_AMBIENT, ambient)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT2, GL_SPECULAR, specular)

    set_light_position()
    #update_light_position(0,0,0)

    #glMaterialfv(GL_FRONT, GL_EMISSION, (0, 0, 0, 1))

    # Position the light (x, y, z, w)
    # w is 1 for directional light (sun), 1 for point light

def set_light_position():
    glPushMatrix()
    glLoadIdentity()

    glLightfv(GL_LIGHT1, GL_POSITION, (-26, 5.4, -3, 1.0))
    glLightfv(GL_LIGHT2, GL_POSITION, (-41.5, 5.4, -3, 1.0))

    glPopMatrix()

def update_light_position(x, y, z):
    light1_position = (-26, 5.4, -3)
    light2_position = (-41.5, 5.4, -3)

    glPushMatrix()
    glLoadIdentity()

    glLightfv(GL_LIGHT1, GL_POSITION, (light1_position[0], light1_position[1], light1_position[2], 1.0))
    glLightfv(GL_LIGHT2, GL_POSITION, (light2_position[0], light2_position[1], light2_position[2], 1.0))

    glPopMatrix()
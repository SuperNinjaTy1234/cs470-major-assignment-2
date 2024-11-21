from OpenGL.GL import *

edges = (
    (-50, -0, 50),
    (50, -0, 50),
    (50, -0, -50),
    (-50, -0, -50)
)

def ground():
    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)

    for edge in edges:
        glVertex3fv(edge)

    glEnd()
    glFlush()

cube_edges = (
    (-0.5,-0.5,0.5),
    (0.5,-0.5,0.5),
    (0.5,0.5,0.5),
    (-0.5,0.5,0.5),
    (-0.5,0.5,-0.5),
    (-0.5, -0.5, -0.5),
    (0.5, -0.5, -0.5),
    (0.5, 0.5, -0.5),
    (-0.5, 0.5, -0.5),
    (-0.5, -0.5, -0.5),
    (-0.5, -0.5, 0.5),
    (0.5, -0.5, 0.5),
    (0.5, -0.5, -0.5),
    (0.5, 0.5, -0.5),
    (0.5, 0.5, 0.5),
    (-0.5, 0.5, 0.5),
    (-0.5, -0.5, 0.5)
)

def cube():
    glBegin(GL_QUADS)
    glColor3f(0, .75, 1)

    for edge in cube_edges:
        glVertex3fv(edge)

    glEnd()
    glFlush()
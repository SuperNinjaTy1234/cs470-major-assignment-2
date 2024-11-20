from OpenGL.GL import *

edges = (
    (-500, -0, 50),
    (500, -0, 50),
    (-500, -0, -500),
    (500, -0, -500)
)

def ground():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)

    for edge in edges:
        glVertex3fv(edge)

    glEnd()
    glFlush()
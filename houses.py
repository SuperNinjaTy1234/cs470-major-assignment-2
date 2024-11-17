from OpenGL.GL import *

edges = (
    (-0.5, 0.5, 0),
    (-0.5, -0.5, 0),
    (0.5, -0.5, 0),
    (0.5, 0.5, 0)
)

def test_house():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_QUADS)
    glColor3f(0, 0, 1)

    for edge in edges:
        glVertex3fv(edge)

    glEnd()
    glFlush()
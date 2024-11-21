from OpenGL.GL import *

road_plane_edges = (
    (-15, -0, 2),
    (15, -0, 2),
    (15, -0, -2),
    (-15, -0, -2)
)

sidewalk_edges = (
    (-15, -0, 3),
    (15, -0, 3),
    (15, -0, -3),
    (-15, -0, -3)
)

yellow_line_edges = (
    (-1, -0, 0.5),
    (1, -0, 0.5),
    (1, -0, -0.5),
    (-1, -0, -0.5)
)

def draw_road():
    side_walk()
    road_plane()
    draw_yellow_lines()

def draw_yellow_lines():
    yellow_line()

    for x in range(4):
        glPushMatrix()
        glTranslate(4 * x, 0, 0)
        yellow_line()
        glPopMatrix()

    for x in range(4):
        glPushMatrix()
        glTranslate(-4 * x, 0, 0)
        yellow_line()
        glPopMatrix()

def road_plane():
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)

    for edge in road_plane_edges:
        glVertex3fv(edge)

    glEnd()
    glFlush()

def side_walk():
    glBegin(GL_QUADS)
    glColor3f(0.7, 0.7, 0.7)

    for edge in sidewalk_edges:
        glVertex3fv(edge)

    glEnd()
    glFlush()

def yellow_line():
    glBegin(GL_QUADS)
    glColor3f(1, 1, 0)

    for edge in yellow_line_edges:
        glVertex3fv(edge)

    glEnd()
    glFlush()
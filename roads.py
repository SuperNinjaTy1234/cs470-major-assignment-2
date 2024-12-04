from OpenGL.GL import *

road_plane_edges = (
    (-5, 0.03, 2),
    (5, 0.03, 2),
    (5, 0.03, -2),
    (-5, 0.03, -2)
)

sidewalk_edges = (
    (-5, 0.02, 3),
    (5, 0.02, 3),
    (5, 0.02, -3),
    (-5, 0.02, -3)
)


def draw_road():
    draw_road_plane()
    draw_road_intersection()

def draw_road_plane():
    segment_length = 10
    left_segments = 11
    right_segments = 11
    for i in range(left_segments):
        offset = i * segment_length
        glPushMatrix()
        glTranslatef(-offset, 0, 0)
        side_walk()
        road_plane()
        glPopMatrix()

    for i in range(right_segments):
        offset = i * segment_length
        glPushMatrix()
        glTranslatef(offset, 0, 0)
        side_walk()
        road_plane()
        glPopMatrix()


def draw_road_intersection():
    segment_length = 10
    left_segments = 5
    right_segments = 11

    #left intersection
    glPushMatrix()
    glTranslatef(-50, -0.01, 0)
    glRotatef(90, 0, 1, 0)
    intersection_sidewalk()

    glPushMatrix()
    glTranslatef(0, 0.021, 0)
    intersection_roads()
    glPopMatrix()

    for i in range(left_segments):
       offset = i * segment_length + 10
       glPushMatrix()
       glTranslatef(-offset, 0, 0)
       intersection_sidewalk()
       intersection_roads()
       glPopMatrix()

    for i in range(right_segments):
       offset = i * segment_length + 10
       glPushMatrix()
       glTranslatef(offset, 0, 0)
       intersection_sidewalk()
       intersection_roads()
       glPopMatrix()
    glPopMatrix()

    #right intersection
    glPushMatrix()
    glTranslatef(50, -0.01, 0)
    glRotatef(90, 0, 1, 0)
    intersection_sidewalk()

    glPushMatrix()
    glTranslatef(0, 0.021, 0)
    intersection_roads()
    glPopMatrix()
    for i in range(left_segments):
       offset = i * segment_length + 10
       glPushMatrix()
       glTranslatef(-offset, 0, 0)
       intersection_sidewalk()
       intersection_roads()
       glPopMatrix()

    for i in range(right_segments):
       offset = i * segment_length + 10
       glPushMatrix()
       glTranslatef(offset, 0, 0)
       intersection_sidewalk()
       intersection_roads()
       glPopMatrix()
    glPopMatrix()

    #back left intersection
    glPushMatrix()
    glTranslatef(-50, -0.01, -25)
    side_walk()

    glPushMatrix()
    glTranslatef(0, 0.021, 0)
    road_plane()
    glPopMatrix()
    for i in range(left_segments):
       offset = i * segment_length + 10
       glPushMatrix()
       glTranslatef(-offset, 0, 0)
       side_walk()
       road_plane()
       glPopMatrix()

    for i in range(right_segments+4):
       offset = i * segment_length + 10
       glPushMatrix()
       glTranslatef(offset, 0, 0)
       side_walk()
       road_plane()
       glPopMatrix()

    glPopMatrix()
def road_plane():
    glPushAttrib(GL_LIGHTING_BIT | GL_CURRENT_BIT)
    glDisable(GL_COLOR_MATERIAL)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.1, 0.1, 0.1, 0.0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.2, 0.2, 0.2, 1.0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1, 1, 1, 1.0])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 25.0)

    glBegin(GL_QUADS)

    for edge in road_plane_edges:
        glVertex3fv(edge)

    glEnd()
    glFlush()
    glEnable(GL_COLOR_MATERIAL)
    glPopAttrib()

def side_walk():
    glPushAttrib(GL_LIGHTING_BIT | GL_CURRENT_BIT)
    glDisable(GL_COLOR_MATERIAL)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.1, 0.1, 0.1, 0.0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.7, 0.7, 0.7, 1.0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1, 1, 1, 1.0])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 25.0)

    glBegin(GL_QUADS)
    for edge in sidewalk_edges:
        glVertex3fv(edge)

    glEnd()
    glFlush()
    glPopAttrib()

def intersection_roads():
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.3, 0.3)
    for edge in road_plane_edges:
        glVertex3fv(edge)

    glEnd()
    glFlush()

def intersection_sidewalk():
    glBegin(GL_QUADS)
    glColor3f(0.7, 0.7, 0.7)
    for edge in sidewalk_edges:
        glVertex3fv(edge)

    glEnd()
    glFlush()
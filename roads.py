from OpenGL.GL import *

road_plane_edges = (
    (-15, 0.03, 2),
    (15, 0.03, 2),
    (15, 0.03, -2),
    (-15, 0.03, -2)
)

sidewalk_edges = (
    (-15, 0.02, 3),
    (15, 0.02, 3),
    (15, 0.02, -3),
    (-15, 0.02, -3)
)

yellow_line_edges = (
    (-1, 0.04, 0.5),
    (1, 0.04, 0.5),
    (1, 0.04, -0.5),
    (-1, 0.04, -0.5)
)

def draw_road():
    draw_road_plane()
    draw_road_intersection() #this function draws more than the road intersection as of now

def draw_side_walk():
    side_walk()

    glPushMatrix()
    glTranslatef(-30, 0, 0)
    side_walk()
    glPopMatrix()

def draw_road_plane():
    #Draws road directly in front of the camera
    side_walk()
    road_plane()
    draw_yellow_lines()

    glPushMatrix()
    glTranslate(-30, 0, 0)
    side_walk()
    road_plane()
    draw_yellow_lines()
    glPopMatrix()

    #Draws road behind the road above
    glPushMatrix()
    glTranslate(0, 0, -60)
    side_walk()
    road_plane()
    draw_yellow_lines()

    glPushMatrix()
    glTranslate(-30, 0, 0)
    side_walk()
    road_plane()
    draw_yellow_lines()
    glPopMatrix()

    glPopMatrix()

#Reusable function for drawing the yellow lines of a road
def draw_yellow_lines():
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

def draw_road_intersection():
    #Draws the left intersection
    glPushMatrix()
    glTranslate(-45, 0, 0)
    side_walk()
    glRotatef(90, 0, 1, 0)  # Rotate to set other side_walk plane
    side_walk()
    glRotate(-90, 0, 1, 0)  # Rotate back to continue as normal
    road_plane()
    draw_yellow_lines()
    glRotatef(90, 0, 1, 0)
    road_plane()
    draw_yellow_lines()

    #Draws the road going back from the left intersection
    glPushMatrix()
    glTranslate(30, 0, 0)
    side_walk()
    road_plane()
    draw_yellow_lines()
    glPopMatrix()

    glPopMatrix()

    #Draws the right intersection
    glPushMatrix()
    glTranslate(30, 0, 0)
    side_walk()
    glRotatef(90, 0, 1, 0)  # Rotate to set other side_walk plane
    side_walk()
    glRotate(-90, 0, 1, 0)  # Rotate back to continue as normal
    road_plane()
    draw_yellow_lines()
    glRotatef(90, 0, 1, 0)
    road_plane()
    draw_yellow_lines()

    #Draws the road going back from the right intersection
    glPushMatrix()
    glTranslate(30, 0, 0)
    side_walk()
    road_plane()
    draw_yellow_lines()
    glPopMatrix()

    glPopMatrix()

    # Draws the right-back intersection
    glPushMatrix()
    glTranslate(30, 0, -60)
    side_walk()
    glRotatef(90, 0, 1, 0)  # Rotate to set other side_walk plane
    side_walk()
    glRotate(-90, 0, 1, 0)  # Rotate back to continue as normal
    road_plane()
    draw_yellow_lines()
    glRotatef(90, 0, 1, 0)
    road_plane()
    draw_yellow_lines()
    glPopMatrix()

    # Draws the left-back intersection
    glPushMatrix()
    glTranslate(-45, 0, -60)
    side_walk()
    glRotatef(90, 0, 1, 0)  # Rotate to set other side_walk plane
    side_walk()
    glRotate(-90, 0, 1, 0)  # Rotate back to continue as normal
    road_plane()
    draw_yellow_lines()
    glRotatef(90, 0, 1, 0)
    road_plane()
    draw_yellow_lines()
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
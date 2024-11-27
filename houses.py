from OpenGL.GL import *


def draw_house():
    # Main house structure
    glBegin(GL_QUADS)
    glColor3f(0.96, 0.96, 0.86)  # Pale Beige color for the wall

    # Bottom section of the front face
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(-1, 0, 1)

    # Top-left section of the front face
    glVertex3f(-1, 0, 1)
    glVertex3f(0.25, 0, 1)
    glVertex3f(0.25, 1, 1)
    glVertex3f(-1, 1, 1)

    # Top-right section of the front face
    glVertex3f(0.75, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(0.75, 1, 1)

    # Back face
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    # Right face
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)

    # Left face
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)

    # Bottom face (floor)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    glEnd()

    # Roof
    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0.8, 0.8)  # Light Grey color for the roof
    # Right side
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(0, 2, 0)

    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(0, 2, 0)

    # Left side
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(0, 2, 0)

    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)
    glVertex3f(0, 2, 0)
    glEnd()

    # Doors
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.1, 0.1)
    # Front door
    glVertex3f(-0.2, -1, 1.1)
    glVertex3f(0.2, -1, 1.1)
    glVertex3f(0.2, -0.2, 1.1)
    glVertex3f(-0.2, -0.2, 1.1)

    # Back door
    glVertex3f(-0.2, -1, -1.1)
    glVertex3f(0.2, -1, -1.1)
    glVertex3f(0.2, -0.2, -1.1)
    glVertex3f(-0.2, -0.2, -1.1)
    glEnd()

    # Windows
    glColor4f(0, 0, 0, 0)
    glBegin(GL_QUADS)
    # Left Window
    glVertex3f(-0.9, 0, 0.8)
    glVertex3f(-0.6, 0, 0.8)
    glVertex3f(-0.6, 0.3, 0.8)
    glVertex3f(-0.9, 0.3, 0.8)
    # Right Window
    glVertex3f(0.6, 0, 0.8)
    glVertex3f(0.9, 0, 0.8)
    glVertex3f(0.9, 0.3, 0.8)
    glVertex3f(0.6, 0.3, 0.8)
    glEnd()


def draw_house4():


    # Main house structure
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.8, 0.85)  # Pale Beige color for the wall

    # Bottom section of the front face
    glVertex3f(-2, -2, 2)
    glVertex3f(2, -2, 2)
    glVertex3f(2, 0, 2)
    glVertex3f(-2, 0, 2)

    # Top-left section of the front face
    glVertex3f(-2, 0, 2)
    glVertex3f(0.5, 0, 2)
    glVertex3f(0.5, 2, 2)
    glVertex3f(-2, 2, 2)

    # Top-right section of the front face
    glVertex3f(1.5, 0, 2)
    glVertex3f(2, 0, 2)
    glVertex3f(2, 2, 2)
    glVertex3f(1.5, 2, 2)

    # Back face
    glVertex3f(-2, -2, -2)
    glVertex3f(2, -2, -2)
    glVertex3f(2, 2, -2)
    glVertex3f(-2, 2, -2)

    # Right face
    glVertex3f(2, -2, -2)
    glVertex3f(2, -2, 2)
    glVertex3f(2, 2, 2)
    glVertex3f(2, 2, -2)

    # Left face
    glVertex3f(-2, -2, -2)
    glVertex3f(-2, -2, 2)
    glVertex3f(-2, 2, 2)
    glVertex3f(-2, 2, -2)

    # Bottom face (floor)
    glVertex3f(-2, -2, -2)
    glVertex3f(2, -2, -2)
    glVertex3f(2, -2, 2)
    glVertex3f(-2, -2, 2)

    glEnd()

    # Roof
    glBegin(GL_TRIANGLES)
    glColor3f(0.3, 0.3, 0.35)  # Light Grey color for the roof
    # Right side
    glVertex3f(-2, 2, 2)
    glVertex3f(2, 2, 2)
    glVertex3f(0, 4, 0)

    glVertex3f(-2, 2, -2)
    glVertex3f(2, 2, -2)
    glVertex3f(0, 4, 0)

    # Left side
    glVertex3f(-2, 2, 2)
    glVertex3f(-2, 2, -2)
    glVertex3f(0, 4, 0)

    glVertex3f(2, 2, 2)
    glVertex3f(2, 2, -2)
    glVertex3f(0, 4, 0)
    glEnd()

    # Doors
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.1, 0.1)
    # Front door
    glVertex3f(-0.5, -2, 2.2)
    glVertex3f(0.5, -2, 2.2)
    glVertex3f(0.5, -0.4, 2.2)
    glVertex3f(-0.5, -0.4, 2.2)

    # Back door
    glVertex3f(-0.4, -2, -2.2)
    glVertex3f(0.4, -2, -2.2)
    glVertex3f(0.4, -0.4, -2.2)
    glVertex3f(-0.4, -0.4, -2.2)
    glEnd()

    # Windows
    glColor4f(0, 0, 0, 0)
    glBegin(GL_QUADS)
    # Left Window
    glVertex3f(-1.8, 0, 1.6)
    glVertex3f(-1.2, 0, 1.6)
    glVertex3f(-1.2, 0.6, 1.6)
    glVertex3f(-1.8, 0.6, 1.6)
    # Right Window
    glVertex3f(1.2, 0, 1.6)
    glVertex3f(1.8, 0, 1.6)
    glVertex3f(1.8, 0.6, 1.6)
    glVertex3f(1.2, 0.6, 1.6)
    glEnd()


def house():
    glPushMatrix()
    glTranslatef(0, 1, -10)  # Move the house further from the camera
    draw_house()
    glPopMatrix()


def house2():
    glPushMatrix()
    glTranslatef(3, 1, -10)  # Move the house further from the camera
    draw_house()
    glPopMatrix()


def house3():
    glPushMatrix()
    glTranslatef(-3, 1, -10)  # Move the house further from the camera
    draw_house()
    glPopMatrix()


def house4():
    glPushMatrix()
    glTranslatef(10, 1, -10)  # Move the house further from the camera
    draw_house4()
    glPopMatrix()


def house5():
    glPushMatrix()
    glTranslatef(-10, 1, -10)  # Move the house further from the camera
    draw_house4()
    glPopMatrix()


def house6():
    glPushMatrix()
    glTranslatef(15, 1, -10)  # Move the house further from the camera
    draw_house4()
    glPopMatrix()

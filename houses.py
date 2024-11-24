from OpenGL.GL import *

def draw_house():
    #glEnable(GL_DEPTH_TEST)
    #glDepthFunc(GL_LESS)

    glEnable(GL_COLOR_MATERIAL)  # Enable material coloring
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    # Main house structure
    glBegin(GL_QUADS)
    glColor3f(0.96, 0.96, 0.86)  # Pale Beige color for the wall

    # Front face
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

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

def test_house():
    glPushMatrix()
    glTranslatef(0, 1, -10)  # Move the house further from the camera
    draw_house()
    glPopMatrix()


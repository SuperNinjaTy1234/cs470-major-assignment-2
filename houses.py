from OpenGL.GL import *

# Garage door animation variables
# garage_door_position = 0
# garage_door_opening = False


def draw_wall():
    # Draw a single wall.
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.5, 0.3)  # Brown for walls
    glVertex3f(-5, 0, 0)  # Bottom left
    glVertex3f(5, 0, 0)   # Bottom right
    glVertex3f(5, 5, 0)   # Top right
    glVertex3f(-5, 5, 0)  # Top left
    glEnd()


def draw_garage_door():
    # Draw the garage door.
    glPushMatrix()

    glBegin(GL_QUADS)
    glColor3f(0.9, 0.9, 0.9)  # Light gray for garage door
    glVertex3f(-2.5, 0, 0)  # Bottom left
    glVertex3f(2.5, 0, 0)   # Bottom right
    glVertex3f(2.5, 2.5, 0)  # Top right
    glVertex3f(-2.5, 2.5, 0)  # Top left
    glEnd()
    glPopMatrix()


def draw_roof():
    # Draw the roof as a triangular prism.
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.2, 0.1)  # Dark brown for roof
    glVertex3f(-5, 5, 5)   # Front left
    glVertex3f(5, 5, 5)    # Front right
    glVertex3f(0, 7.5, 0)  # Peak
    glVertex3f(-5, 5, -5)  # Back left
    glVertex3f(5, 5, -5)   # Back right
    glVertex3f(0, 7.5, 0)  # Peak
    glEnd()


def draw_window():
    # Draw a single window.
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.8, 1.0)  # Light blue for windows
    glVertex3f(-1, 3.5, 0)   # Bottom left
    glVertex3f(1, 3.5, 0)    # Bottom right
    glVertex3f(1, 4.5, 0)    # Top right
    glVertex3f(-1, 4.5, 0)   # Top left
    glEnd()


def draw_house():
    # Assemble the house using transformations.
    glPushMatrix()

    # Front wall with garage door and window
    glPushMatrix()
    glTranslatef(0, 0, 5)  # Position the front wall
    draw_wall()
    draw_garage_door()
    glPushMatrix()
    glTranslatef(-3, 0, 0)  # Position the window on the wall
    draw_window()
    glPopMatrix()
    glPopMatrix()

    # Back wall
    glPushMatrix()
    glTranslatef(0, 0, -5)  # Position the back wall
    draw_wall()
    glPopMatrix()

    # Left wall
    glPushMatrix()
    glTranslatef(-5, 0, 0)  # Position the left wall
    glRotatef(90, 0, 1, 0)  # Rotate to make it a side wall
    draw_wall()
    glPopMatrix()

    # Right wall
    glPushMatrix()
    glTranslatef(5, 0, 0)  # Position the right wall
    glRotatef(90, 0, 1, 0)  # Rotate to make it a side wall
    draw_wall()
    glPopMatrix()

    # Roof
    draw_roof()

    glPopMatrix()


# def animate_garage_door():
import pygame
from OpenGL.GL import *


def load_skybox_textures():
    textures = glGenTextures(5)  # Generate only five textures
    files = ['top.jpg', 'front.jpg', 'back.jpg', 'left.jpg', 'right.jpg']  # List only five sides
    path = "Background_imgs/"
    skybox_faces = []

    for i, file in enumerate(files):
        img_path = path + file
        img = pygame.image.load(img_path)
        if img is None:
            print(f"Error loading image: {img_path}")
            continue  # Skip if image not loaded

        texture = textures[i]
        glBindTexture(GL_TEXTURE_2D, texture)
        img_data = pygame.image.tostring(img, "RGBA", 1)
        width, height = img.get_size()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        skybox_faces.append(texture)

    return skybox_faces


def draw_skybox(skybox_textures):
    glEnable(GL_TEXTURE_2D)

    # Define vertices for each face of the cube, omitting the bottom face
    vertices = [
        # Top
        [-50, 50, -50], [50, 50, -50], [50, 50, 50], [-50, 50, 50],
        # Front
        [-50, -50, 50], [50, -50, 50], [50, 50, 50], [-50, 50, 50],
        # Right
        [50, -50, 50], [50, -50, -50], [50, 50, -50], [50, 50, 50],
        # Back
        [50, -50, -50], [-50, -50, -50], [-50, 50, -50], [50, 50, -50],
        # Left
        [-50, -50, -50], [-50, -50, 50], [-50, 50, 50], [-50, 50, -50]
    ]

    # Define the order in which vertices will be used for each face
    indices = [(0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15), (16, 17, 18, 19)]

    # Draw each face with the appropriate texture
    for i, face in enumerate(indices):
        glBindTexture(GL_TEXTURE_2D, skybox_textures[i])
        glBegin(GL_QUADS)
        for vertex in face:
            glTexCoord2f(0 if vertex % 4 in [0, 3] else 1, 0 if vertex % 4 in [0, 1] else 1)
            glVertex3fv(vertices[vertex])
        glEnd()

    glDisable(GL_TEXTURE_2D)


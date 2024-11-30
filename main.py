
#The main file of the program
import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *

#imports of specific models
from ground_plane import *
from body_of_water import *
from houses import *
from roads import *
from light import setup_daylight, enable_nighttime_lighting, enable_daytime_lighting
from background import load_texture
from scene_object import SceneObject

# If you are importing through blender, use the SceneObject like below and it will take care of everything.
# It already will render because there is a for loop that loops through all scene objects
imported_house1 = SceneObject("Models/House.obj", scaled_size=4,name="imported_house1")
door1 = SceneObject('Models/door.obj', scaled_size=1.6, name="door1")
imported_house2 = SceneObject("Models/House2.obj", scaled_size=4, name="imported_house2")
door2 = SceneObject("Models/door2.obj", scaled_size=1.6, name="door2")
grocery_store = SceneObject("Models/grocery_store.obj", scaled_size=5, name="grocery_store")
barn = SceneObject("Models/barn.obj", scaled_size=5, name="barn")
street_light1 = SceneObject("Models/street_lights.obj", scaled_size=5, name="street_lights")
street_light2 = SceneObject("Models/street_lights.obj", scaled_size=5, name="street_lights")
barnDoor = SceneObject("Models/barnDoor.obj", scaled_size=2.3, name="door3")
scene_objects = [
    {"object": imported_house1, "position": (8, 2.05, -7), "rotation": (0, 270, 0)},
    {"object": door1, "position": (8, 0.9, -5.3), "rotation": (0, 270, 0)},
    {"object": imported_house2, "position": (-7, 2, -7), "rotation": (0, 270, 0)},
    {"object": door2, "position": (-7, 0.9, -5.3), "rotation": (0, 270, 0)},
    {"object": grocery_store, "position": (-35, 1.5, -5), "rotation": (0, 0, 0)},
    {"object": barn, "position": (-17.5, 2.5, -10), "rotation": (0, 0, 0)},
    {"object": street_light1, "position": (-26, 2.4, -3.5), "rotation": (0, -90, 0)},
    {"object": street_light2, "position": (-41.5, 2.4, -3.5), "rotation": (0, -90, 0)},
    {"object": barnDoor, "position": (-17, 1.1, -8.1), "rotation": (0, 0, 0)},
]

# Had to implement major changes to camera in order for positions to work correctly
# so doors could be opened and eventually a car can be moved
class Camera:
    def __init__(self):
        self.position = np.array([0.0, 2.0, 10.0], dtype=np.float64)  # Initial position
        self.target = np.array([0.0, 0.0, 0.0], dtype=np.float64)  # Look at origin
        self.up = np.array([0.0, 1.0, 0.0], dtype=np.float64)  # Up direction

        # Movement flags
        self.move_x = 0
        self.move_y = 0
        self.move_z = 0
        self.rotate_horizontal = 0
        self.rotate_vertical = 0

        self.speed = 8.0
        self.rotation_speed = 60.0

    def update_position(self, delta_time):
        forward = self.target - self.position
        forward[1] = 0
        forward /= np.linalg.norm(forward)  # Normalize

        dx = self.move_x * self.speed * delta_time
        dy = self.move_y * self.speed * delta_time
        dz = self.move_z * self.speed * delta_time

        self.position += forward * dz
        self.position[0] += dx
        self.position[1] += dy

        self.target += forward * dz
        self.target[0] += dx
        self.target[1] += dy


    def rotate_camera(self, delta_time):
        if self.rotate_horizontal or self.rotate_vertical:
            if self.rotate_horizontal != 0:
                angle = np.radians(self.rotate_horizontal * self.rotation_speed * delta_time)
                rotation_matrix = np.array([
                    [np.cos(angle), 0, np.sin(angle)],
                    [0, 1, 0],
                    [-np.sin(angle), 0, np.cos(angle)],
                ])
                direction = self.target - self.position
                self.target = self.position + np.dot(rotation_matrix, direction)

            if self.rotate_vertical != 0:
                angle = np.radians(self.rotate_vertical * self.rotation_speed * delta_time)
                rotation_matrix = np.array([
                    [1, 0, 0],
                    [0, np.cos(angle), -np.sin(angle)],
                    [0, np.sin(angle), np.cos(angle)],
                ])
                direction = self.target - self.position
                direction = np.dot(rotation_matrix, direction)

                direction[1] = np.clip(direction[1], -10, 10)
                self.target = self.position + direction


def toggle_visible_doors(camera):
    door_objects = [obj for obj in scene_objects if "door" in obj["object"].name.lower()]
    closest_door = None
    closest_distance = float("inf")

    for obj in door_objects:
        scene_obj = obj["object"]
        door_position = np.array(obj["position"])

        is_visible = is_door_visible(camera, door_position)
        print(f"{scene_obj.name} at {door_position} is {'visible' if is_visible else 'not visible'}")

        if is_visible:
            distance = np.linalg.norm(door_position - camera.position)
            if distance < closest_distance:
                closest_door = scene_obj
                closest_distance = distance

    if closest_door:
        closest_door.open = not closest_door.open
        print(f"Toggled {closest_door.name}. New state: {'Open' if closest_door.open else 'Closed'}")


def is_door_visible(camera, door_position):
    to_door = door_position - camera.position
    to_door /= np.linalg.norm(to_door)  # Normalize

    forward = camera.target - camera.position
    forward /= np.linalg.norm(forward)  # Normalize
    if np.dot(forward, to_door) <= 0:
        return False
    fov_cosine = np.cos(np.radians(45))
    if np.dot(forward, to_door) < fov_cosine:
        return False

    distance = np.linalg.norm(door_position - camera.position)
    if distance > 15:
        return False
    return True

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    bg_texture = load_texture("Textures/mountain.jpg")  # Load the mountain texture
    camera = Camera()
    setup_daylight()  # Start with daylight

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glEnable(GL_COLOR_MATERIAL)


    is_daytime = True  # Lighting state
    clock = pygame.time.Clock()
    while True:
        delta_time = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    camera.move_x = -1
                elif event.key == pygame.K_d:
                    camera.move_x = 1
                elif event.key == pygame.K_s:
                    camera.move_z = -1
                elif event.key == pygame.K_w:
                    camera.move_z = 1
                elif event.key == pygame.K_r:
                    camera.rotate_horizontal = -1
                elif event.key == pygame.K_q:
                    camera.rotate_horizontal = 1
                elif event.key == pygame.K_m:
                    camera.rotate_vertical = 1
                elif event.key == pygame.K_n:
                    camera.rotate_vertical = -1
                elif event.key == pygame.K_UP:
                    camera.move_y = 1
                elif event.key == pygame.K_DOWN:
                    camera.move_y = -1
                elif event.key == pygame.K_o:
                    toggle_visible_doors(camera)
                elif event.key is pygame.K_t:  # Toggle lighting
                    is_daytime = not is_daytime
                    if is_daytime:
                        enable_daytime_lighting()
                    else:
                        enable_nighttime_lighting()
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_a, pygame.K_d):
                    camera.move_x = 0
                elif event.key in (pygame.K_w, pygame.K_s):
                    camera.move_z = 0
                elif event.key in (pygame.K_q, pygame.K_r):
                    camera.rotate_horizontal = 0
                elif event.key in (pygame.K_m, pygame.K_n):
                    camera.rotate_vertical = 0
                elif event.key in (pygame.K_UP, pygame.K_DOWN):
                    camera.move_y = 0

        camera.update_position(delta_time)
        camera.rotate_camera(delta_time)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(
            camera.position[0], camera.position[1], camera.position[2],
            camera.target[0], camera.target[1], camera.target[2],
            camera.up[0], camera.up[1], camera.up[2]
        )

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        ground()
        glPushAttrib(GL_ALL_ATTRIB_BITS)
        draw_water_plane()
        glPopAttrib()
        draw_road()
        house()
        house2()
        house3()

        for obj in scene_objects:
            obj["object"].render(position=obj["position"], rotation=obj["rotation"], open_rotation=90)

        pygame.display.flip()

main()

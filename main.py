import math

#The main file of the program
import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *

from background import init_opengl, draw_background, load_texture
#imports of specific models
from ground_plane import *
from body_of_water import *
from houses import *
from roads import *
from light import setup_daylight, enable_nighttime_lighting, enable_daytime_lighting
from scene_object import SceneObject

# If you are importing through blender, use the SceneObject like below and it will take care of everything.
# It already will render because there is a for loop that loops through all scene objects
imported_house1 = SceneObject("Models/House.obj", scaled_size=4,name="imported_house1")
door1 = SceneObject('Models/door.obj', scaled_size=1.6, name="door1")
imported_house2 = SceneObject("Models/House2.obj", scaled_size=4, name="imported_house2")
door2 = SceneObject("Models/door2.obj", scaled_size=1.6, name="door2")
imported_house3 = SceneObject("Models/House3.obj", scaled_size=4, name="imported_house3")
door3 = SceneObject("Models/door3.obj", scaled_size=1.65, name="door3")
imported_house4 = SceneObject("Models/House4.obj", scaled_size=4, name="imported_house4")
door4 = SceneObject("Models/door4.obj", scaled_size=1.67, name="door4")
grocery_store = SceneObject("Models/grocery_store.obj", scaled_size=5, name="grocery_store")
barn = SceneObject("Models/barn.obj", scaled_size=5, name="barn")
street_light1 = SceneObject("Models/street_lights.obj", scaled_size=5, name="street_lights")
street_light2 = SceneObject("Models/street_lights.obj", scaled_size=5, name="street_lights")
barnDoor = SceneObject("Models/barnDoor.obj", scaled_size=2.3, name="door5")
cat = SceneObject("Models/cat.obj", scaled_size=1.5, name="cat")
catLeg1 = SceneObject("Models/catLeg1.obj", scaled_size=0.4, name="catLeg1")
catLeg2 = SceneObject("Models/catLeg1.obj", scaled_size=0.4, name="catLeg2")
catLeg3 = SceneObject("Models/catLeg1.obj", scaled_size=0.4, name="catLeg3")
catLeg4 = SceneObject("Models/catLeg1.obj", scaled_size=0.4, name="catLeg4")
trees = SceneObject("Models/trees.obj", scaled_size=5, name="trees")
car = SceneObject("Models/Car.obj", scaled_size=5, name="car")
scene_objects = [
    {"object": imported_house1, "position": (8, 2.05, -7), "rotation": (0, 270, 0)},
    {"object": door1, "position": (8, 0.9, -5.3), "rotation": (0, 270, 0)},
    {"object": imported_house2, "position": (-7, 2, -7), "rotation": (0, 270, 0)},
    {"object": door2, "position": (-7, 0.9, -5.3), "rotation": (0, 270, 0)},
    {"object": imported_house3, "position": (-2,1.9, -7), "rotation": (0, 270, 0)},
    {"object": door3, "position": (-1.95, 0.9, -5.1), "rotation": (0, 270, 0)},
    {"object": imported_house4, "position": (2.7,2.05, -7), "rotation": (0, 270, 0)},
    {"object": door4, "position": (2.7, 0.95, -5.1), "rotation": (0, 270, 0)},
    {"object": grocery_store, "position": (-35, 1.3, -5), "rotation": (0, 0, 0)},
    {"object": barn, "position": (-17.5, 2.5, -10), "rotation": (0, 0, 0)},
    {"object": street_light1, "position": (-26, 2.4, -3.5), "rotation": (0, -90, 0)},
    {"object": street_light2, "position": (-41.5, 2.4, -3.5), "rotation": (0, -90, 0)},
    {"object": barnDoor, "position": (-17, 1.1, -8.1), "rotation": (0, 0, 0)},
    {"object": cat, "position": (-9, 0.8, -4.0), "rotation": (0, 180, 0)},
    {"object": trees, "position": (-12, 2.4, -8.3), "rotation": (0, 0, 0)},
    {"object": catLeg1, "position": (-9.3, 0.2, -3.9), "rotation": (0, 0, 0)},
    {"object": catLeg2, "position": (-9.3, 0.2, -4.1), "rotation": (0, 0, 0)},
    {"object": catLeg3, "position": (-8.7, 0.2, -3.9), "rotation": (0, 0, 0)},
    {"object": catLeg4, "position": (-8.7, 0.2, -4.1), "rotation": (0, 0, 0)},
    {"object": car, "position": (-25,1.2, 0), "rotation": (0, 180, 0)},
]

def toggle_visible_doors(camera_position, camera_target):
    door_objects = [obj for obj in scene_objects if "door" in obj["object"].name.lower()]
    closest_door = None
    closest_distance = float("inf")

    for obj in door_objects:
        scene_obj = obj["object"]
        door_position = np.array(obj["position"])

        is_visible = is_door_visible(camera_position, camera_target, door_position)

        if is_visible:
            distance = np.linalg.norm(door_position - camera_position)
            if distance < closest_distance:
                closest_door = scene_obj
                closest_distance = distance

    if closest_door:
        closest_door.open = not closest_door.open


def is_door_visible(camera_position, camera_target, door_position):
    forward = camera_target - camera_position
    forward /= np.linalg.norm(forward)

    to_door = door_position - camera_position
    to_door /= np.linalg.norm(to_door)

    fov_cosine = np.cos(np.radians(45))
    if np.dot(forward, to_door) < fov_cosine:
        return False

    distance = np.linalg.norm(door_position - camera_position)
    if distance > 15:
        return False
    return True

def main():
    pygame.init()
    display = (800, 600)
    init_opengl(display)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    background_texture = load_texture("Background_imgs/front.jpg")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    camera_position = np.array([0.0, 2.0, 10.0])
    camera_target = np.array([0.0, 0.0, 0.0])
    camera_up = np.array([0.0, 1.0, 0.0])
    move_x = move_y = move_z = rotate_horizontal = rotate_vertical = 0

    move_car = 0
    speed = 9.0
    rotation_speed = 65.0

    setup_daylight()  # Start with daylight

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glEnable(GL_COLOR_MATERIAL)

    animation_time = 0.0
    stop_time = 40.0
    is_animating = True

    is_daytime = True  # Lighting state
    clock = pygame.time.Clock()
    while True:
        delta_time = clock.tick(60) / 1000.0

        #Animations
        animation_time += delta_time
        if animation_time >= stop_time:
            is_animating = False
        if is_animating:
            angle = math.sin(animation_time * 4.0) * 30
            for obj in scene_objects:
                if obj["object"].name == "catLeg1":
                    obj["rotation"] = (0, 0, angle)
                    obj["position"] = (obj["position"][0] + 0.05, obj["position"][1], obj["position"][2])
                elif obj["object"].name == "catLeg2":
                    obj["rotation"] = (0, 0, -angle)
                    obj["position"] = (obj["position"][0] + 0.05, obj["position"][1], obj["position"][2])
                elif obj["object"].name == "catLeg3":
                    obj["rotation"] = (0, 0, -angle)
                    obj["position"] = (obj["position"][0] + 0.05, obj["position"][1], obj["position"][2])
                elif obj["object"].name == "catLeg4":
                    obj["rotation"] = (0, 0, angle)
                    obj["position"] = (obj["position"][0] + 0.05, obj["position"][1], obj["position"][2])
                elif obj["object"].name == "cat":
                    obj["position"] = (obj["position"][0]+0.05, obj["position"][1], obj["position"][2])

        if move_car == 1:
            for obj in scene_objects:
                if obj["object"].name == "car":
                    obj["position"] = (obj["position"][0] + 0.5, obj["position"][1], obj["position"][2])
        if move_car == -1:
            for obj in scene_objects:
                if obj["object"].name == "car":
                    obj["position"] = (obj["position"][0] - 0.5, obj["position"][1], obj["position"][2])
        #Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_x = 1
                elif event.key == pygame.K_d:
                    move_x = -1
                elif event.key == pygame.K_s:
                    move_z = -1
                elif event.key == pygame.K_w:
                    move_z = 1
                elif event.key == pygame.K_r:
                    rotate_horizontal = -1
                elif event.key == pygame.K_q:
                    rotate_horizontal = 1
                elif event.key == pygame.K_m:
                    rotate_vertical = 1
                elif event.key == pygame.K_n:
                    rotate_vertical = -1
                elif event.key == pygame.K_RIGHT:
                    move_car = 1
                elif event.key == pygame.K_LEFT:
                    move_car = -1
                elif event.key == pygame.K_UP:
                    move_y = 1
                elif event.key == pygame.K_DOWN:
                    move_y = -1
                elif event.key == pygame.K_o:
                    toggle_visible_doors(camera_position, camera_target)
                elif event.key == pygame.K_t:  # Toggle lighting
                    is_daytime = not is_daytime
                    if is_daytime:
                        enable_daytime_lighting()
                    else:
                        enable_nighttime_lighting()
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_a, pygame.K_d):
                    move_x = 0
                elif event.key in (pygame.K_w, pygame.K_s):
                    move_z = 0
                elif event.key in (pygame.K_q, pygame.K_r):
                    rotate_horizontal = 0
                elif event.key in (pygame.K_m, pygame.K_n):
                    rotate_vertical = 0
                elif event.key in (pygame.K_UP, pygame.K_DOWN):
                    move_y = 0
                elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    move_car = 0

        forward = camera_target - camera_position
        forward /= np.linalg.norm(forward)

        movement_forward = forward.copy()
        movement_forward[1] = 0
        movement_forward /= np.linalg.norm(movement_forward)

        right = np.array([forward[2], 0, -forward[0]])
        right /= np.linalg.norm(right)

        camera_position += movement_forward * move_z * speed * delta_time
        camera_position += right * move_x * speed * delta_time
        camera_position[1] += move_y * speed * delta_time

        camera_target = camera_position + forward

        if rotate_horizontal != 0:
            angle = np.radians(rotate_horizontal * rotation_speed * delta_time)
            rotation_matrix = np.array([
                [np.cos(angle), 0, np.sin(angle)],
                [0, 1, 0],
                [-np.sin(angle), 0, np.cos(angle)],
            ])
            forward = np.dot(rotation_matrix, forward)
            camera_target = camera_position + forward

        if rotate_vertical != 0:
            angle = np.radians(rotate_vertical * rotation_speed * delta_time)
            rotation_matrix = np.array([
                [1, 0, 0],
                [0, np.cos(angle), -np.sin(angle)],
                [0, np.sin(angle), np.cos(angle)],
            ])
            forward = np.dot(rotation_matrix, forward)
            camera_target = camera_position + forward


        glLoadIdentity()
        gluLookAt(
            camera_position[0], camera_position[1], camera_position[2],
            camera_target[0], camera_target[1], camera_target[2],
            camera_up[0], camera_up[1], camera_up[2]
        )
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_background(background_texture)

        glPushMatrix()
        ground()
        glPushAttrib(GL_ALL_ATTRIB_BITS)
        draw_water_plane()
        glPopAttrib()
        draw_road()
        glPopMatrix()

        for obj in scene_objects:
            obj["object"].render(position=obj["position"], rotation=obj["rotation"], open_rotation=90)
        pygame.display.flip()

main()

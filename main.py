import math
import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GLU import *
from background import init_opengl, draw_background, load_texture
from ground_plane import *
from body_of_water import *
from roads import *
from light import enable_nighttime_lighting, enable_daytime_lighting, light_init
from scene_object import SceneObject

imported_house1 = SceneObject("Models/House.obj", scaled_size=4,name="imported_house1")
door1 = SceneObject('Models/door.obj', scaled_size=1.6, name="door1")
door1b = SceneObject('Models/door.obj', scaled_size=1.6, name="door1b")
imported_house2 = SceneObject("Models/House2.obj", scaled_size=4, name="imported_house2")
door2 = SceneObject("Models/door2.obj", scaled_size=1.6, name="door2")
door2b = SceneObject("Models/door2.obj", scaled_size=1.6, name="door2b")
imported_house3 = SceneObject("Models/House3.obj", scaled_size=4, name="imported_house3")
door3 = SceneObject("Models/door3.obj", scaled_size=1.65, name="door3")
door3b = SceneObject("Models/door3.obj", scaled_size=1.65, name="door3b")
imported_house4 = SceneObject("Models/House4.obj", scaled_size=4, name="imported_house4")
door4 = SceneObject("Models/door4.obj", scaled_size=1.67, name="door4")
door4b = SceneObject("Models/door4.obj", scaled_size=1.67, name="door4b")
grocery_store = SceneObject("Models/Grocery_Store.obj", scaled_size=8, name="grocery_store")
garage_door = SceneObject("Models/garage.obj", scaled_size=3, name="garage")
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
human = SceneObject("Models/Human.obj", scaled_size=2, name="human")
arm = SceneObject("Models/Arm.obj", scaled_size=0.6, name="arm")
scene_objects = [
    {"object": imported_house1, "position": (8, 2.05, -7), "rotation": (0, 270, 0)},
    {"object": door1, "position": (8, 0.9, -5.3), "rotation": (0, 270, 0)},
    {"object": door1b, "position": (8, 0.9, -8.8), "rotation": (0, 90, 0)},
    {"object": imported_house2, "position": (-7, 2.05, -7), "rotation": (0, 270, 0)},
    {"object": door2, "position": (-7, 0.9, -5.3), "rotation": (0, 270, 0)},
    {"object": door2b, "position": (-6.9, 0.9, -8.8), "rotation": (0, 90, 0)},
    {"object": imported_house3, "position": (-2,1.9, -7), "rotation": (0, 270, 0)},
    {"object": door3, "position": (-1.92, 0.9, -5.18), "rotation": (0, 270, 0)},
    {"object": door3b, "position": (-1.92, 0.9, -8.9), "rotation": (0, 90, 0)},
    {"object": imported_house4, "position": (2.7,2.05, -7), "rotation": (0, 270, 0)},
    {"object": door4, "position": (2.74, 0.95, -5.18), "rotation": (0, 270, 0)},
    {"object": door4b, "position": (2.74, 0.95, -8.9), "rotation": (0, 90, 0)},
    {"object": grocery_store, "position": (-35, 2.6, -7), "rotation": (0, 0, 0)},
    {"object": garage_door, "position": (-35.1, 1, -4.2), "rotation": (0, 0, 0)},
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
    {"object": human, "position": (-23,1, -8), "rotation": (0, 90, 0)},
    {"object": arm, "position": (-23,1.22, -8.4), "rotation": (0, 90, 0)},
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

def animate_garage_door( camera_position, camera_target, open_state):
    for obj in scene_objects:
        if obj["object"].name == "garage":
            position = np.array(obj["position"])
            visible = is_door_visible(camera_position, camera_target, position)
            if visible:
                if open_state:
                    obj["position"] = (obj["position"][0], obj["position"][1] + 1.26, obj["position"][2])
                    obj["rotation"] = (90, obj["rotation"][1], obj["rotation"][2])
                else:
                    obj["position"] = (-35.1, 1, -4.2)
                    obj["rotation"] = (0, 0, 0)

def rotate_human_towards_camera(camera_position, human_position):
    direction_to_camera = camera_position - human_position
    direction_to_camera[1] = 0
    direction_to_camera /= np.linalg.norm(direction_to_camera)

    angle = np.degrees(np.arctan2(direction_to_camera[0], direction_to_camera[2]))
    return angle

def is_visible(camera_position, camera_target, human_position):
    forward = camera_target - camera_position
    forward /= np.linalg.norm(forward)

    to_human = human_position - camera_position
    to_human /= np.linalg.norm(to_human)

    fov_cosine = np.cos(np.radians(45))

    if np.dot(forward, to_human) < fov_cosine:
        return False

    distance = np.linalg.norm(human_position - camera_position)
    if distance > 10:
        return False

    return True

def rotate_point_around_center(point, center, angle):
    angle_rad = math.radians(angle)
    x_point, z = point[0] - center[0], point[1] - center[1]
    x_new = x_point * math.cos(angle_rad) - z * math.sin(angle_rad)
    z_new = x_point  * math.sin(angle_rad) + z * math.cos(angle_rad)
    return x_new + center[0], z_new + center[1]

def main():
    pygame.init()
    display = (800, 600)
    init_opengl(display)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    background_texture = load_texture("Background_imgs/front.jpg")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    camera_position = np.array([0.0, 2.0, 10.0])
    camera_target = np.array([0.0, 0.0, 0.0])
    camera_up = np.array([0.0, 1.0, 0.0])
    move_x = move_y = move_z = rotate_horizontal = rotate_vertical = 0

    move_car = 0
    speed = 9.0
    rotation_speed = 65.0
    glEnable(GL_LIGHTING)
    enable_daytime_lighting()  # Start with daylight

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glEnable(GL_COLOR_MATERIAL)
    garage_open_state = False
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

        for obj in scene_objects:
            if obj["object"].name == "human":
                human_position = np.array(obj["position"])
                if is_visible(camera_position, camera_target, human_position):
                    target_rotation = rotate_human_towards_camera(camera_position, human_position)
                    current_rotation = obj["rotation"][1]  # Get current Y rotation
                    if abs(target_rotation - current_rotation) > 0:
                        if target_rotation > current_rotation:
                            current_rotation += rotation_speed * delta_time
                        elif target_rotation < current_rotation:
                            current_rotation -= rotation_speed * delta_time

                        if abs(current_rotation - target_rotation) < rotation_speed * delta_time:
                            current_rotation = target_rotation

                    obj["rotation"] = (0, current_rotation, 0)
                    for arm_obj in scene_objects:
                        if arm_obj["object"].name == "arm":
                            arm_offset = np.array([0.47, 0.6, 0.14])
                            arm_local_position = human_position + arm_offset

                            # Rotate the arm's local position around the human
                            rotated_xz = rotate_point_around_center(
                                (arm_local_position[0], arm_local_position[2]),
                                (human_position[0], human_position[2]),
                                -current_rotation
                            )

                            # Update the arm's world position
                            arm_obj["position"] = (rotated_xz[0], arm_local_position[1], rotated_xz[1])

                            wave_angle = math.sin(animation_time * 4.0) * 10
                            arm_obj["rotation"] = (0,current_rotation,160 + wave_angle)
                else:
                    obj["rotation"] = (0, 90, 0)
                    for arm_obj in scene_objects:
                        if arm_obj["object"].name == "arm":
                            arm_obj["position"] = (-23,1.22, -8.4)
                            arm_obj["rotation"] = (0, 90, 0)

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
                    garage_open_state = not garage_open_state
                    animate_garage_door(camera_position, camera_target, garage_open_state)
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


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(
            camera_position[0], camera_position[1], camera_position[2],
            camera_target[0], camera_target[1], camera_target[2],
            camera_up[0], camera_up[1], camera_up[2]
        )

        light_init(is_daytime)
        glPushMatrix()
        draw_background(background_texture)
        ground()
        glPushAttrib(GL_ALL_ATTRIB_BITS)
        draw_water_plane()
        glPopAttrib()
        draw_road()
        for obj in scene_objects:
            obj["object"].render(position=obj["position"], rotation=obj["rotation"], open_rotation=90)
        glPopMatrix()
        pygame.display.flip()

main()

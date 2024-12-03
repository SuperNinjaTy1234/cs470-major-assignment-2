import math
import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GLU import *

from animations import toggle_visible_doors, animate_garage_door, animate_human_and_arm, animate_cat, car_movement
from background import init_opengl, draw_background, load_texture
from ground_plane import *
from body_of_water import *
from roads import *
from light import enable_nighttime_lighting, enable_daytime_lighting, light_init
from scene_object import scene_objects


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
        animation_time += delta_time
        if animation_time >= stop_time:
            is_animating = False
        if is_animating:
            animate_cat(animation_time)

        car_movement(move_car)
        animate_human_and_arm(camera_position, camera_target, animation_time, rotation_speed, delta_time)

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

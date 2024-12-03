import math
import numpy as np
from helpers import is_door_visible, rotate_human_towards_camera, is_visible, rotate_point_around_center
from scene_object import scene_objects


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

def animate_human_and_arm( camera_position, camera_target, animation_time, rotation_speed, delta_time):
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
                        arm_obj["rotation"] = (0, current_rotation, 160 + wave_angle)
            else:
                obj["rotation"] = (0, 90, 0)
                for arm_obj in scene_objects:
                    if arm_obj["object"].name == "arm":
                        arm_obj["position"] = (-23, 1.22, -8.4)
                        arm_obj["rotation"] = (0, 90, 0)

def toggle_visible_doors(camera_position, camera_target):
    door_objects = [obj for obj in scene_objects if "door" in obj["object"].name.lower()]
    closest_door = None
    closest_distance = float("inf")

    for obj in door_objects:
        scene_obj = obj["object"]
        door_position = np.array(obj["position"])

        visible = is_door_visible(camera_position, camera_target, door_position)

        if visible:
            distance = np.linalg.norm(door_position - camera_position)
            if distance < closest_distance:
                closest_door = scene_obj
                closest_distance = distance

    if closest_door:
        closest_door.open = not closest_door.open

def animate_cat(animation_time):
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
            obj["position"] = (obj["position"][0] + 0.05, obj["position"][1], obj["position"][2])

def car_movement(move_car):
    if move_car == 1:
        for obj in scene_objects:
            if obj["object"].name == "car":
                obj["position"] = (obj["position"][0] + 0.5, obj["position"][1], obj["position"][2])
    if move_car == -1:
        for obj in scene_objects:
            if obj["object"].name == "car":
                obj["position"] = (obj["position"][0] - 0.5, obj["position"][1], obj["position"][2])

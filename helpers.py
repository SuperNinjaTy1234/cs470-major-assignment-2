import math
import numpy as np

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

def vertical_rotation(rotate_vertical, rotation_speed, delta_time, camera_position, forward):
    angle = np.radians(rotate_vertical * rotation_speed * delta_time)
    right = np.cross(forward, np.array([0.0, 1.0, 0.0]))

    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)

    rotation_matrix = np.array([
        [cos_angle + right[0] * right[0] * (1 - cos_angle),
         right[0] * right[1] * (1 - cos_angle) - right[2] * sin_angle,
         right[0] * right[2] * (1 - cos_angle) + right[1] * sin_angle],
        [right[1] * right[0] * (1 - cos_angle) + right[2] * sin_angle,
         cos_angle + right[1] * right[1] * (1 - cos_angle),
         right[1] * right[2] * (1 - cos_angle) - right[0] * sin_angle],
        [right[2] * right[0] * (1 - cos_angle) - right[1] * sin_angle,
         right[2] * right[1] * (1 - cos_angle) + right[0] * sin_angle,
         cos_angle + right[2] * right[2] * (1 - cos_angle)],
    ])
    forward = np.dot(rotation_matrix, forward)
    return camera_position + forward

def horizontal_rotation (rotate_horizontal, rotation_speed, delta_time, camera_position, forward):
    angle = np.radians(rotate_horizontal * rotation_speed * delta_time)
    rotation_matrix = np.array([
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)],
    ])
    forward = np.dot(rotation_matrix, forward)
    return camera_position + forward
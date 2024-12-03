import numpy as np
from OpenGL.GL import *
import pywavefront

class SceneObject:
    def __init__(self, model_path, scaled_size, name=None):

        self.model = pywavefront.Wavefront(model_path, collect_faces=True)
        self.name = name if name else model_path
        bbox_min = np.min(self.model.vertices, axis=0)
        bbox_max = np.max(self.model.vertices, axis=0)
        self.bounding_box = (bbox_min, bbox_max)

        self.size = bbox_max - bbox_min
        self.max_size = np.max(self.size)
        self.scale = [scaled_size / self.max_size for _ in range(3)]
        self.translation = -((bbox_max + bbox_min) / 2)

        self.open = False

        self.hinge_offset = (0.45, 0, 0)
    def render(self, position, rotation=(0, 0, 0), open_rotation=None):
        glPushMatrix()
        glTranslate(*position)
        glRotatef(rotation[0], 1, 0, 0)
        glRotatef(rotation[1], 0, 1, 0)
        glRotatef(rotation[2], 0, 0, 1)

        if self.open and open_rotation:
            glTranslate(*self.hinge_offset)
            glRotatef(open_rotation, 0, 1, 0)
            glTranslate(self.hinge_offset[0], self.hinge_offset[1], self.hinge_offset[2])

        self.render_object()
        glPopMatrix()

    def render_object(self):
        glPushMatrix()
        glScalef(*self.scale)
        glTranslatef(*self.translation)

        for mesh in self.model.mesh_list:
            material_name = mesh.materials[0].name
            material = self.model.materials.get(material_name)

            glColor(material.diffuse)
            glBegin(GL_TRIANGLES)
            for face in mesh.faces:
                for vertex_i in face:
                    glVertex3f(*self.model.vertices[vertex_i])
            glEnd()

        glPopMatrix()

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

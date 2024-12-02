import numpy as np
from OpenGL.GL import *
import pywavefront


class SceneObject:
    def __init__(self, model_path, scaled_size, name=None):
        """
              Initialize a SceneObject with its model data and scaling.

              Parameters:
                  model_path (str): Path to the model file.
                  scaled_size (float): Desired maximum size after scaling.
        """

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
        """
        Render the object at a given position with optional rotation.

        Parameters:
            position (tuple): World position (x, y, z).
            rotation (tuple): Rotation angles (x, y, z) in degrees.
            open_rotation (float): Additional rotation if the object is "open."
        """
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
        """
        Internal method to render the object using its scale and translation.
        """
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


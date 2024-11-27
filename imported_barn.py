from OpenGL.GL import *
import pywavefront

# Imports a Grocery Store
barn = pywavefront.Wavefront('Models/Barn.obj', collect_faces=True)

scene_box = (barn.vertices[0], barn.vertices[0])
for vertex in barn.vertices:
    min_v = [min(scene_box[0][i], vertex[i]) for i in range(3)]
    max_v = [max(scene_box[1][i], vertex[i]) for i in range(3)]
    scene_box = (min_v, max_v)

scene_size     = [scene_box[1][i]-scene_box[0][i] for i in range(3)]
max_scene_size = max(scene_size)
scaled_size    = 5
scene_scale    = [scaled_size/max_scene_size for i in range(3)]
scene_trans    = [-(scene_box[1][i]+scene_box[0][i])/2 for i in range(3)]

def draw_imported_barn():
    glPushMatrix()
    glTranslate(-17.5, 2.5, -10)
    draw_barn()
    glPopMatrix()

def draw_barn():
    glPushMatrix()
    glScalef(*scene_scale)
    glTranslatef(*scene_trans)

    for mesh in barn.mesh_list:
        material_name = mesh.materials[0].name  # Get the material name
        material = barn.materials.get(material_name)

        glColor(material.diffuse)

        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*barn.vertices[vertex_i])
        glEnd()

    glPopMatrix()

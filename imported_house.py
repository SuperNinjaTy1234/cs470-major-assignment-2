from OpenGL.GL import *
import pywavefront


imported_house = pywavefront.Wavefront('Models/House.obj', collect_faces=True)

scene_box = (imported_house.vertices[0], imported_house.vertices[0])
for vertex in imported_house.vertices:
    min_v = [min(scene_box[0][i], vertex[i]) for i in range(3)]
    max_v = [max(scene_box[1][i], vertex[i]) for i in range(3)]
    scene_box = (min_v, max_v)

scene_size     = [scene_box[1][i]-scene_box[0][i] for i in range(3)]
max_scene_size = max(scene_size)
scaled_size    = 3
scene_scale    = [scaled_size/max_scene_size for i in range(3)]
scene_trans    = [-(scene_box[1][i]+scene_box[0][i])/2 for i in range(3)]

def draw_imported_house():
    glPushMatrix()
    glTranslate(14,1.5,-7)
    glRotate(270,0,1,0)
    render_house()
    glPopMatrix()

def render_house():
    glPushMatrix()
    glScalef(*scene_scale)
    glTranslatef(*scene_trans)

    for mesh in imported_house.mesh_list:
        material_name = mesh.materials[0].name  # Get the material name
        material = imported_house.materials.get(material_name)

        glColor(material.diffuse)

        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*imported_house.vertices[vertex_i])
        glEnd()

    glPopMatrix()
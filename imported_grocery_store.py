from OpenGL.GL import *
import pywavefront

# Imports a Grocery Store
groceryStore = pywavefront.Wavefront('Models/Grocery_Store.obj', collect_faces=True)

scene_box = (groceryStore.vertices[0], groceryStore.vertices[0])
for vertex in groceryStore.vertices:
    min_v = [min(scene_box[0][i], vertex[i]) for i in range(3)]
    max_v = [max(scene_box[1][i], vertex[i]) for i in range(3)]
    scene_box = (min_v, max_v)

scene_size     = [scene_box[1][i]-scene_box[0][i] for i in range(3)]
max_scene_size = max(scene_size)
scaled_size    = 5
scene_scale    = [scaled_size/max_scene_size for i in range(3)]
scene_trans    = [-(scene_box[1][i]+scene_box[0][i])/2 for i in range(3)]

def draw_imported_grocery_store():
    glPushMatrix()
    glTranslate(-35, 1.5, -5)
    grocery_store()
    glPopMatrix()

def grocery_store():
    glPushMatrix()
    glScalef(*scene_scale)
    glTranslatef(*scene_trans)

    glColor3f(0, 0.2, 0.2)

    for mesh in groceryStore.mesh_list:
        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*groceryStore.vertices[vertex_i])
        glEnd()

    glPopMatrix()

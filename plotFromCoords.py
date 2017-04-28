## Begin file plotFromCoords.py
## Created by Gregory Croisdale March 2017
## CreatePT for Computer Science Principles

## library importation
import bpy, bmesh, os
from mathutils import Vector, kdtree
from math import tan
from time import sleep

scn = bpy.context.scene

## determines the number with the most distance from zero
def absMax(list):
    return max([max(map(float, list)), abs(min(map(float, list)))])

## turns coordinate file into list
def listIn(directory):
    i = open(directory + ".coord", "r")
    return i.read().split(",")

## selects all vertices
def selectVert():
    for v in mesh.verts:
        v.select = True

## plots and fills function according to table output
def plotFunction(name, x, y, edge):
    ## Create new mesh in default location
    me = bpy.data.meshes.new(name)
    ob = bpy.data.objects.new(name, me)
    me.update()
    scn.objects.link(ob)
    scn.objects.active = ob
    ob.select = True
    bpy.data.objects[name].location = (0, 0, 0)

    ## get file input
    os.chdir("F:/revolutionaryPy/")
    xVal = listIn(x)
    yVal = listIn(y)

    ## plot data and generate mesh
    bm = bmesh.new()
    bm.from_mesh(bpy.context.object.data)
    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    for i in range(0,len(xVal) - 1):
        bm.verts.new([float(xVal[i]),0.0,float(yVal[i])])
        bm.to_mesh(bpy.context.object.data)

    ## prepares for filling
    bpy.ops.object.mode_set(mode='EDIT', toggle=False)
    bmf = bmesh.from_edit_mesh(bpy.context.object.data).verts

    if edge:  ## creates edges between vertices
        for j in range(0,len(bmf) - 2):
            bmf.ensure_lookup_table()
            bmf[j].select = True
            bmf[j + 1].select = True
            bpy.ops.mesh.edge_face_add()
            bpy.ops.mesh.select_all(action = 'DESELECT')
    else:  ## creates face between vertices
        bpy.ops.mesh.select_all(action = 'SELECT')
        bpy.ops.mesh.edge_face_add()

    ## finalizes object
    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

plotFunction("f(x)", "x", "f", True)
plotFunction("g(x)", "x", "g", True)
plotFunction("intersect", "xi", "i", False)

y = listIn('i')
x = listIn('xi')

## exports and sets origin
bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')

## creates and adjusts camera
cY = max([absMax(y), absMax(x)]) / tan(1/3)
cam = bpy.ops.object.camera_add(view_align=False, enter_editmode=False, location=(0.0, cY, 0.0), rotation=(270.0*0.01745329251,180.0*0.01745329251,0.0))
bpy.data.cameras[0].lens = 1/3 * 100

## preps scene for rendering
scn.render.resolution_y = 1920; scn.render.resolution_x = 1920
scr = bpy.context.window.screen
v3d = [area for area in scr.areas if area.type == 'VIEW_3D'][0]
v3d.spaces[0].pivot_point = 'CURSOR'
scn.render.image_settings.file_format = 'PNG'
bpy.context.scene.camera = bpy.data.objects['Camera']
## Begin file plotFromCoords.py

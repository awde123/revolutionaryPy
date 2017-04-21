## Created by Gregory Croisdale March 2017
## CreatePT for Computer Science Principles

import bpy, bmesh, os, math
from mathutils import Vector, kdtree

## determines the number with the most distance from zero
def absMax(list):
    return max([max(map(float, list)), abs(min(map(float, list)))])

## turns file into list
def listIn(directory): 
    i = open(directory, "r")
    return i.read().split(",")

## selects all vertices
def selectVert(): 
    for v in mesh.verts:
        v.select = True

def plotFunction(name, x, y):
    ## Create new mesh
    me = bpy.data.meshes.new(name)
    ob = bpy.data.objects.new(name, me)
    me.update()
    scn = bpy.context.scene
    scn.objects.link(ob)
    scn.objects.active = ob
    ob.select = True
    bpy.data.objects[name].location = (0, 0, 0)
    
    ## get file input
    os.chdir("/Users/s97507/plot/revolutionaryPy/")
    xVal = listIn(x)
    yVal = listIn(y)
    
    ## plot data and generate mesh
    bm = bmesh.new()
    bm.from_mesh(bpy.context.object.data)
    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    for i in range(0,len(xVal) - 1):
        bm.verts.new([float(xVal[i]),0.0,float(yVal[i])])
        bm.to_mesh(bpy.context.object.data)
        
    bpy.ops.object.mode_set(mode='EDIT', toggle=False)
    bmf = bmesh.from_edit_mesh(bpy.context.object.data).verts
    for j in range(0,len(bmf) - 2):
        bmf.ensure_lookup_table()
        bmf[j].select = True
        bmf[j + 1].select = True
        bpy.ops.mesh.edge_face_add()
        bpy.ops.mesh.select_all(action = 'DESELECT')

    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

plotFunction("f(x)", "x", "f")
plotFunction("g(x)", "x", "g")
plotFunction("intersect", "xi", "i")

y = listIn('f') + listIn('g')
x = listIn('x')

## exports and sets origin
bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')

## sets camera y value
bpy.data.objects['Camera'].location.y = max([absMax(y), absMax(x)]) / math.sin(1/3)

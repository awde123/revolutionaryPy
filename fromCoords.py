## Created by Gregory Croisdale March 2017
## CreatePT for Computer Science Principles

import bpy, bmesh, os, math
from mathutils import Vector, kdtree

os.chdir("/Users/s97507/plot/revolutionaryPy/")

bpy.data.objects['Function'].location = (0, 0, 0)

def absMax(list): ## determines the number with the most distance from zero
    return max([max(map(float, list)), abs(min(map(float, list)))])

def newBMesh():
    ## initial mesh generation code
    bm = bmesh.new()
    bm.from_mesh(bpy.context.object.data)
    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

def plot(x, y): ## plots vertices according to x and y arrays
    bm = bmesh.new()
    bm.from_mesh(bpy.context.object.data)
    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    for i in range(0,len(x) - 1):
        bm.verts.new([float(x[i]),0.0,float(y[i])])
        bm.to_mesh(bpy.context.object.data)
    ## exports meshdata to object
    bpy.ops.object.mode_set(mode='EDIT', toggle=False)

def listIn(directory): ## turns file into array
    i = open(directory, "r")
    return i.read().split(",")

def selectVert(): ## selects all vertices
    for v in mesh.verts:
        v.select = True
        
size = len(bm.verts)
kd = kdtree.KDTree(size)

obj = bpy.context.edit_object
me = obj.data
bm = bmesh.from_edit_mesh(me)

plot(listIn('x'),listIn('f'))

plot(listIn('x'),listIn('g'))

y = listIn('f') + listIn('g')

x = listIn('x')

## exports and sets origin
bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')

## sets camera y value
bpy.data.objects['Camera'].location.y = max([absMax(y), absMax(x)]) / math.sin(0.5)

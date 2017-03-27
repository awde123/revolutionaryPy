import bpy, bmesh, os, math

def absMax(list):
    return max([max(map(float, list)), abs(min(map(float, list)))])

## inputs x and y value from external files
x = open(os.getcwd() + "\\x.txt", "r")
y = open(os.getcwd() + "\\y.txt", "r")

## creates lists from external data
xval = x.read().split(",")
yval = y.read().split(",")

## initial mesh generation code
bm = bmesh.new()
bm.from_mesh(bpy.context.object.data)
bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

## creates vertices from x and y lists
for i in range(0,len(xval) - 1):
    bm.verts.new([float(xval[i]),0.0,float(yval[i])])
    bm.to_mesh(bpy.context.object.data)

## exports meshdata to object
bpy.ops.object.mode_set(mode='EDIT', toggle=False)
mesh=bmesh.from_edit_mesh(bpy.context.object.data)


## creates single face from all verticies
for v in mesh.verts:
    v.select = True
bpy.ops.mesh.edge_face_add()

## exports and sets origin
bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')

## sets camera y value

bpy.data.objects['Camera'].location.y = max([absMax(yval), absMax(xval)]) / math.sin(0.5)

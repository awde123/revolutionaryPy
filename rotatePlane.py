## Created by Gregory Croisdale March 2017
## CreatePT for Computer Science Principles
import bpy, bmesh
import math
from time import sleep

scene = bpy.context.scene
fp = scene.render.filepath # get existing output path
scene.render.image_settings.file_format = 'PNG' # set output format to .png

def get_override(area_type, region_type):
    for area in bpy.context.screen.areas: 
        if area.type == area_type:             
            for region in area.regions:                 
                if region.type == region_type:                    
                    override = {'area': area, 'region': region} 
                    return override
    #error message if the area or region wasn't found
    raise RuntimeError("Wasn't able to find", region_type," in area ", area_type,
                        "\n Make sure it's open while executing script.")

override = get_override( 'VIEW_3D', 'WINDOW' )

for x in range(0,360):
    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    scene.frame_set(x)
    scene.render.filepath = fp + str(x)
    bpy.ops.render.render(write_still=True)
    bpy.ops.object.mode_set(mode='EDIT', toggle=False)
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 0)})
    bpy.ops.transform.rotate(override, value=math.pi/180, axis=(1,0,0))

ob = bpy.data.objects['area']
mesh=bmesh.from_edit_mesh(bpy.context.object.data)
for v in mesh.verts:
    v.select = True
bpy.ops.mesh.remove_doubles()

scene.render.filepath = fp

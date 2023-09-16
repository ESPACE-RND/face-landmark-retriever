# Generates vertices from a list of coordinates in an Excel file

import bpy
import pandas as pd
from ast import literal_eval
import bmesh

# Path to your Excel file
excel_file_path = ""

# Read the Excel file
df = pd.read_excel(excel_file_path)

# Set the frame range based on the number of rows in the Excel file
start_frame = bpy.context.scene.frame_start
end_frame = start_frame + len(df) - 1
frame__anim_rate = 1

# Create a new mesh and object
mesh = bpy.data.meshes.new("MyMesh")
obj = bpy.data.objects.new("MyObject", mesh)

# Link the object to the scene
scene = bpy.context.scene
scene.collection.objects.link(obj)

# Select the object
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

# Enter Edit Mode to create vertices
bpy.ops.object.mode_set(mode='EDIT')

# Create vertices
bm = bmesh.from_edit_mesh(mesh)
verts = []  # Define vertex coordinates

# Create points based on the coordinates
for index, row in df.iterrows():
    count = 0
    for x in  literal_eval(row[0]):
        x, y, z = x[0], x[1], x[2]
        verts.append((x,y,z))
    break


for v in verts:
    bm.verts.new(v)

# Update the mesh with the new vertices
bmesh.update_edit_mesh(mesh)

bpy.ops.object.mode_set(mode='OBJECT')
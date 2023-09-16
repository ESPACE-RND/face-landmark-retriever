# Animates the detected landmarks

import bpy
import pandas as pd
from ast import literal_eval

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

# Set keyframes for each sphere's location for each frame
frame = 1

# Get the mesh data
obj = bpy.data.objects.get("MyObject")     
mesh = obj.data

action = bpy.data.actions.new("MeshAnimation")

mesh.animation_data_create()
mesh.animation_data.action = action


for i in range(0,len(df),frame__anim_rate):
    print(i)
    bpy.context.scene.frame_set(frame)
    count = 0
    for x in  literal_eval(df.loc[i, 0]):
        vertex = mesh.vertices[count]  
        
        x, y, z = x[0], x[1], x[2]
        
        vertex.co.x = x
        vertex.co.y = y
        vertex.co.z = z
        
        vertex.keyframe_insert("co", index=0)
        vertex.keyframe_insert("co", index=1)
        vertex.keyframe_insert("co", index=2)
    
        count = count + 1
    
    frame = frame + frame__anim_rate
    if (frame > 250):
        break

# Update the scene
bpy.context.view_layer.update()


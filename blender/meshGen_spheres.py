# Generates spheres from a list of coordinates in an Excel file

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
frame__anim_rate = 3

# Create points based on the coordinates
for index, row in df.iterrows():
    count = 0
    for x in  literal_eval(row[0]):
        x, y, z = x[0], x[1], x[2]
        sphere_name = f"sphere_{count}"
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.005, location=(x, y, z))
        bpy.context.object.name = sphere_name
        count = count + 1
    break

# Set keyframes for each sphere's location for each frame
frame = 1
for i in range(0,len(df),frame__anim_rate):
    print(i)
    bpy.context.scene.frame_set(frame)
    count = 0
    for x in  literal_eval(df.loc[i, 0]):
        sphere = bpy.data.objects.get("sphere_"+str(count))       
        x, y, z = x[0], x[1], x[2]
        sphere.location = (x, y, z)
        sphere.keyframe_insert(data_path="location", frame=frame)
        count = count + 1
    frame = frame + frame__anim_rate
    if (frame > 250):
        break

# Update the scene
bpy.context.view_layer.update()
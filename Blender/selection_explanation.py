import bpy
#list all the selected meshes 
mesh_list = bpy.context.selected_objects

#find the object is active( find the last item of the selection list)
parent_obj = bpy.context.active_object
parent_obj_translate_X = parent_obj.location[0]
parent_obj_translate_Y = parent_obj.location[1]
parent_obj_translate_Z = parent_obj.location[2]
#remove the children from the list
children_list = mesh_list.remove(parent_obj)

child_obj = mesh_list[0]

print(parent_obj)

print(child_obj)

child_obj.location[0]= parent_obj_translate_X
child_obj.location[1]= parent_obj_translate_Y
child_obj.location[2]= parent_obj_translate_Z

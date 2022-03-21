import maya.cmds as cmds

#we need a list for geometry selection 
#define which object is the first, which object is the last one. Defining which obj is the child, while which object is the parent. 
#once we define the parent and child. we get the data from the parent object(the last selection), and set the data got from the parenet object to become transform data of the children object.


#create mesh_list from what we have selected now in the viewport.
mesh_list = cmds.ls(selection=True, type="transform")
#mesh_list_shape = cmds.ls(selection=True)

#the last item is the second item of the list
#last_item_hard_number = mesh_list[1]

mesh_idx = len(mesh_list) - 1

last_item = mesh_list[mesh_idx]

#get transform attributes from the last item
translate_X_parent = cmds.getAttr(last_item + ".translateX")
print("{0}'s translate X is {1}".format(last_item, translate_X_parent))

#set transform attributes for the child obj
translate_X_child = cmds.setAttr(mesh_list[0]+".translateX", translate_X_parent)

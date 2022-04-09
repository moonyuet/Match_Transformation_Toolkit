import maya.cmds as cmds


#first object will be the child obj
#last object will be the parent

mesh_list = cmds.ls(selection=True, type="transform")


idx = len(mesh_list)-1
parent_obj = mesh_list[idx]
pv = cmds.xform(parent_obj,piv=True ,q=True)

for i in range(idx):
    if i < idx:
        translate_p_attr_X = cmds.getAttr(mesh_list[i] + ".translateX")
        translate_p_attr_Y = cmds.getAttr(mesh_list[i] + ".translateY")
        translate_p_attr_Z = cmds.getAttr(mesh_list[i] + ".translateZ")
        
        translate_attr_X = cmds.getAttr(parent_obj + ".translateX")
        translate_attr_Y = cmds.getAttr(parent_obj + ".translateY")
        translate_attr_Z = cmds.getAttr(parent_obj + ".translateZ") 

        distance_X = translate_attr_X - translate_p_attr_X
        distance_Y = translate_attr_Y - translate_p_attr_Y
        distance_Z = translate_attr_Z - translate_p_attr_Z

        if pv[0] == 0 and pv[1]== 0 and pv[2] == 0:
                  
            cmds.xform(mesh_list[i], pivots=[distance_X, distance_Y, distance_Z])
        else:
            
            dist_X = pv[0] + distance_X
            dist_Y = pv[1] + distance_Y
            dist_Z = pv[2] + distance_Z
            
            cmds.xform(mesh_list[i], pivots=[dist_X, dist_Y, dist_Z])
            
    else:
        cmds.warning("You must select more than one object!")
            
#if the pivot is already centralized, use the translate attribute
#else use the pivot attributes 
        
        

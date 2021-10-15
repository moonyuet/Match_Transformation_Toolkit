import maya.cmds as cmds

scale = "scale"
translate = "translate"
rotation = "rotate"
############################################
def snap_to_first_selection(transform_type):
	select_obj = cmds.ls(selection= True, type="transform")
	object_number = len(select_obj)

	if not (object_number < 2):
			#get the transform attr from the first object
		template_obj_translateX = cmds.getAttr(select_obj[0] + "." + transform_type + "X")
		template_obj_translateY = cmds.getAttr(select_obj[0] + "." + transform_type + "Y")
		template_obj_translateZ = cmds.getAttr(select_obj[0] + "." + transform_type + "Z")
		
		for i in range(object_number):
		    if i > 0:
			    cmds.setAttr(select_obj[i] + "." + transform_type + "X", template_obj_translateX)
			    cmds.setAttr(select_obj[i] + "." + transform_type + "Y", template_obj_translateY)
			    cmds.setAttr(select_obj[i] + "." + transform_type + "Z", template_obj_translateZ)  
	else:
		 cmds.warning("Select at least two objects")
	
snap_to_first_selection(scale)
snap_to_first_selection(translate)
snap_to_first_selection(rotation)

def matchAllTransformation():
	snap_to_first_selection(scale)
	snap_to_first_selection(translate)
	snap_to_first_selection(rotation)
	
matchAllTransformation()
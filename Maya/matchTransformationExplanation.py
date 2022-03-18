import maya.cmds as cmds

scale = "scale"
translate = "translate"
rotation = "rotate"
############################################
def snap_to_first_selection(transform_type):

	select_obj = cmds.ls(selection= True, type="transform")
	object_number = len(select_obj) #get the number of the object
	if not (object_number < 2):
			#get the transform attr from the parent object(the last object of the object list)
			#Python: select_obj[0] = the frist object and select_obj[1] = the second object 
		template_obj_translateX = cmds.getAttr(select_obj[object_number-1] + "." + transform_type + "X")
		template_obj_translateY = cmds.getAttr(select_obj[object_number-1] + "." + transform_type + "Y")
		template_obj_translateZ = cmds.getAttr(select_obj[object_number-1] + "." + transform_type + "Z")
		
		for i in range(object_number):
		    if i < object_number:  
				#set the transform attirbute of the child object (the first object)
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
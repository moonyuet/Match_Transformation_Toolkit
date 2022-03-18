import bpy

class TransformationPanel(bpy.types.Panel):
    
    bl_label = "Match Transform Toolkit"
    bl_idname = "TRANSFORM_PT_PANEL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Transform Attribute"
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("all.tansform_operator")
        row = layout.row()
        row.operator("match.translation_operator")
        row = layout.row()
        row.operator("match.rotation_operator")
        row = layout.row()
        row.operator("match.scale_operator")    

class matchTransformation(bpy.types.Operator):
    
    bl_label = "Match All Transformations"
    bl_idname = "all.tansform_operator"
    
    def execute(self, context):
        mesh_list = bpy.context.selected_objects

        #find the object is active(the last item of the selection list)
        parent_obj = bpy.context.active_object
        
        #remove the children from the list
        mesh_list.remove(parent_obj)

        
        XYZ = len(parent_obj.location)
        for child_obj in mesh_list:
            for i in range(XYZ):
                child_obj.location[i] = parent_obj.location[i]
                child_obj.rotation_euler[i] = parent_obj.rotation_euler[i]
                child_obj.scale[i] = parent_obj.scale[i]
        
        return {"FINISHED"} 

class matchTranslation(bpy.types.Operator):
    
    bl_label = "Match Translation"
    bl_idname = "match.translation_operator"

    def execute(self, context):
        mesh_list = bpy.context.selected_objects

        #find the object is active(the last item of the selection list)
        parent_obj = bpy.context.active_object
        
        #remove the children from the list
        mesh_list.remove(parent_obj)
        
        XYZ = len(parent_obj.location)
        for child_obj in mesh_list:  
            for i in range(XYZ):
                child_obj.location[i] = parent_obj.location[i]
        
        return {"FINISHED"}  
      
class matchRotation(bpy.types.Operator):
    
    bl_label = "Match Rotation"
    bl_idname = "match.rotation_operator"

    def execute(self, context):
        mesh_list = bpy.context.selected_objects

        #find the object is active(the last item of the selection list)
        parent_obj = bpy.context.active_object
        
        #remove the children from the list
        mesh_list.remove(parent_obj)
        
        XYZ = len(parent_obj.location)
        for child_obj in mesh_list:    
            for i in range(XYZ):
                child_obj.rotation_euler[i] = parent_obj.rotation_euler[i]
        
        return {"FINISHED"}

class matchScale(bpy.types.Operator):
    
    bl_label = "Match Scale"
    bl_idname = "match.scale_operator"

    def execute(self, context):
        mesh_list = bpy.context.selected_objects

        #find the object is active(the last item of the selection list)
        parent_obj = bpy.context.active_object
        
        #remove the children from the list
        mesh_list.remove(parent_obj)
        
        XYZ = len(parent_obj.location)
        for child_obj in mesh_list:
            for i in range(XYZ):
                child_obj.scale[i] = parent_obj.scale[i]
        
        return {"FINISHED"}   

def register():
    bpy.utils.register_class(TransformationPanel)
    bpy.utils.register_class(matchTransformation)
    bpy.utils.register_class(matchTranslation)
    bpy.utils.register_class(matchRotation)
    bpy.utils.register_class(matchScale)
    
def unregister():
    bpy.utils.unregister_class(TransformationPanel)
    bpy.utils.unregister_class(matchTransformation)
    bpy.utils.unregister_class(matchTranslation)
    bpy.utils.unregister_class(matchRotation)
    bpy.utils.unregister_class(matchScale)
if __name__ == "__main__":
    register()
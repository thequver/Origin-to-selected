bl_info = {
    "name": "Origin to Selected",
    "author": "Quver",
    "version": (1, 0),
    "blender": (3, 5, 0),
    "location": "Mesh > Snap",
    "description": "Set object origin to the selected item",
    "category": "Object"
}

import bpy

class OriginToSelected(bpy.types.Operator):
    """Set object origin to the selected item"""
    bl_idname = "mesh.origin_to_selected"
    bl_label = "Origin to Selected"

    def execute(self, context):
        cursor_init_loc = bpy.context.scene.cursor.location.copy()
        bpy.ops.view3d.snap_cursor_to_selected()
        selected_items_count = bpy.context.active_object.data.total_vert_sel + bpy.context.active_object.data.total_edge_sel + bpy.context.active_object.data.total_face_sel
        if selected_items_count == 0:
            self.report({"ERROR"}, "Nothing selected")
            return {'CANCELLED'}

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.context.scene.cursor.location = cursor_init_loc
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OriginToSelected)
    bpy.types.VIEW3D_MT_edit_mesh.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OriginToSelected)
    bpy.types.VIEW3D_MT_edit_mesh.remove(menu_func)

def menu_func(self, context):
    self.layout.operator(OriginToSelected.bl_idname)

if __name__ == "__main__":
    register()
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
from Origin_to_Selected.Origin_to_Selected import *

def register():
    bpy.utils.register_class(OriginToSelected)
    bpy.types.VIEW3D_MT_edit_mesh.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OriginToSelected)
    bpy.types.VIEW3D_MT_edit_mesh.remove(menu_func)

if __name__ == "__main__":
    register()
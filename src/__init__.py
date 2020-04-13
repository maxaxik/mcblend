import bpy
from bpy.props import PointerProperty, BoolProperty, FloatVectorProperty
import bmesh
import mathutils


from .operator import (
    OBJECT_OT_NusiqMcblendExportOperator, OBJECT_OT_NusiqMcblendExportAnimationOperator,
    OBJECT_OT_NusiqMcblendMapUvOperator, OBJECT_OT_NusiqMcblendUvGroupOperator,
    OBJECT_OT_NusiqMcblendToggleMcIsBoneOperator,
    OBJECT_OT_NusiqMcblendToggleMcMirrorOperator,
    OBJECT_OT_NusiqMcblendSetInflateOperator,
    menu_func_nusiq_mcblend_export, menu_func_nusiq_mcblend_export_animation,
    OBJECT_OT_NusiqMcblendRoundDimensionsOperator,
    OBJECT_OT_NusiqMcblendImport, menu_func_nusiq_mcblend_import,
)
from .panel import (
    OBJECT_PT_NusiqMcblendExportPanel,
    OBJECT_NusiqMcblendExporterProperties,
    OBJECT_PT_NusiqMcblendExportAnimationPanel,
    OBJECT_PT_NusiqMcblendSetUvsPanel,
    OBJECT_PT_NusiqMcblendOperatorsPanel,
)


bl_info = {
    "name": "Mcblend",
    "author": "Artur",
    "description": "",
    "blender": (2, 80, 0),
    "version": (3, 1, 2),  # COMPATIBILITY BREAKING CHANGE, NEW FEATURE, BUGFIX
    "location": "",
    "warning": "",
    "category": "Generic"
}


classes = (
    OBJECT_OT_NusiqMcblendExportOperator,
    OBJECT_OT_NusiqMcblendExportAnimationOperator,
    OBJECT_PT_NusiqMcblendExportAnimationPanel,
    OBJECT_PT_NusiqMcblendExportPanel,
    OBJECT_NusiqMcblendExporterProperties,
    OBJECT_OT_NusiqMcblendMapUvOperator,
    OBJECT_PT_NusiqMcblendSetUvsPanel,
    OBJECT_OT_NusiqMcblendUvGroupOperator,
    OBJECT_OT_NusiqMcblendToggleMcIsBoneOperator,
    OBJECT_OT_NusiqMcblendToggleMcMirrorOperator,
    OBJECT_PT_NusiqMcblendOperatorsPanel,
    OBJECT_OT_NusiqMcblendSetInflateOperator,
    OBJECT_OT_NusiqMcblendRoundDimensionsOperator,
    OBJECT_OT_NusiqMcblendImport,
)


def register():
    for _class in classes:
        bpy.utils.register_class(_class)
    bpy.types.Scene.nusiq_mcblend = PointerProperty(
        type=OBJECT_NusiqMcblendExporterProperties
    )
    bpy.types.TOPBAR_MT_file_export.append(menu_func_nusiq_mcblend_export)
    bpy.types.TOPBAR_MT_file_export.append(
        menu_func_nusiq_mcblend_export_animation
    )
    bpy.types.TOPBAR_MT_file_import.append(
        menu_func_nusiq_mcblend_import
    )


def unregister():
    for _class in reversed(classes):
        bpy.utils.unregister_class(_class)
    del bpy.types.Scene.nusiq_mcblend
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_nusiq_mcblend_export)
    bpy.types.TOPBAR_MT_file_export.remove(
        menu_func_nusiq_mcblend_export_animation
    )
    bpy.types.TOPBAR_MT_file_import.remove(
        menu_func_nusiq_mcblend_import
    )


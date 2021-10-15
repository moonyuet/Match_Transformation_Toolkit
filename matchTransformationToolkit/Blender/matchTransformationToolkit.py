import maya.cmds as cmds

def snap_to_first_selection():
    selection = cmds.ls(selection= True, type="transform")
    if len(selection) > 1:
        selection_tx = cmds.getAttr(selection [0] + ".translateX")
        selection_ty = cmds.getAttr(selection [0] + ".translateY")
        selection_tz = cmds.getAttr(selection [0] + ".translateZ")
        for asset in selection[1:]:
            cmds.setAttr(asset + ".translateX", selection_tx)
            cmds.setAttr(asset + ".translateY", selection_ty)
            cmds.setAttr(asset + ".translateZ", selection_tz)
    else:
        cmds.warning("Select at least two objects")
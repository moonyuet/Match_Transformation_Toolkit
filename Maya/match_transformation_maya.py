import sys

from PySide2 import QtCore
#from PySide2 import QtGui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.cmds as cmds
import maya.OpenMayaUI as omui


def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    if sys.version_info.major >= 3:
        return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
    else:
        return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class MatchTransformationPanel(QtWidgets.QDialog):

    WINDOW_TITLE = "Simply Explain Match Transformation"

    def __init__(self, parent=maya_main_window()):
        super(MatchTransformationPanel, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        if cmds.about(ntOS=True):
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        elif cmds.about(macOS=True):
            self.setWindowFlags(QtCore.Qt.Tool)

        self.resize(400, 150)

        self.group_items = []

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.locA_name_le = QtWidgets.QLineEdit()
        self.locA_name_le.setReadOnly(True)
        self.locA_btn = QtWidgets.QPushButton("Print")

        self.locB_name_le = QtWidgets.QLineEdit()
        self.locB_name_le.setReadOnly(True)
        self.locB_btn = QtWidgets.QPushButton("Print")

        self.allTrans_btn = QtWidgets.QPushButton("Match All Transformation")
        self.translate_btn = QtWidgets.QPushButton("Match Translation")
        self.rotate_btn = QtWidgets.QPushButton("Match Rotation")
        self.scale_btn = QtWidgets.QPushButton("Match Scale")

    def create_layout(self):
        locA_layout = QtWidgets.QHBoxLayout()
        locA_layout.addWidget(self.locA_name_le)
        locA_layout.addWidget(self.locA_btn)

        locB_layout = QtWidgets.QHBoxLayout()
        locB_layout.addWidget(self.locB_name_le)
        locB_layout.addWidget(self.locB_btn)

        locA_name_layout = QtWidgets.QFormLayout()
        locA_name_layout.addRow("Mesh A's Pivot Transform: ", locA_layout)

        locB_name_layout = QtWidgets.QFormLayout()
        locB_name_layout.addRow("Mesh B's Pivot Transform: ", locB_layout)
        
        match_btn_layout = QtWidgets.QHBoxLayout()
        match_btn_layout.addWidget(self.allTrans_btn)
        match_btn_layout.addWidget(self.translate_btn)
        match_btn_layout.addWidget(self.rotate_btn)
        match_btn_layout.addWidget(self.scale_btn)

        match_layout = QtWidgets.QFormLayout()
        match_layout.addRow(match_btn_layout)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(1, 1, 1, 1)
        main_layout.addLayout(locA_name_layout)
        main_layout.addLayout(locB_name_layout)
        main_layout.addLayout(match_layout)

    def create_connections(self):
        self.locA_btn.clicked.connect(self.print_loc_a)
        self.locB_btn.clicked.connect(self.print_loc_b)
        self.translate_btn.clicked.connect(self.matchTranslation)
        self.rotate_btn.clicked.connect(self.matchRotation)
        self.scale_btn.clicked.connect(self.matchScale)
        self.allTrans_btn.clicked.connect(self.matchAllTransformation)

    
    def print_loc_a(self):
        transformX =self.readTransform_Parent("translate", "X")
        transformY =self.readTransform_Parent("translate", "Y")
        transformZ =self.readTransform_Parent("translate", "Z")
        self.locA_name_le.setText("Location A: [{0}] [{1}] [{2}]".format(transformX, transformY, transformZ))
    
    def print_loc_b(self):
        transformX =self.readTransform_LocB("translate", "X")
        transformY =self.readTransform_LocB("translate", "Y")
        transformZ =self.readTransform_LocB("translate", "Z")
        self.locB_name_le.setText("Location B: [{0}] [{1}] [{2}]".format(transformX, transformY, transformZ))

#Select the object
    def selection(self):
        return cmds.ls(selection= True, type="transform")

#Find the transform of the parent object
    def readTransform_Parent(self, transform_type, transform_axis):
        sel = self.selection()
        object_number = len(sel)
        if not object_number < 2:
            return cmds.getAttr(sel[object_number-1] + "." + transform_type + transform_axis) #get transform attribute of the first parent object
        else:
            return cmds.warning("Please select more than one mesh")


#Find the transform of the first children object(for printing out value only) 
    def readTransform_LocB(self, transform_type, transform_axis):
        sel = self.selection()
        object_number = len(sel)
        for i in range(object_number):
                
            if i < object_number : 
                return cmds.getAttr(sel[i] + "." + transform_type + transform_axis) #get transform attribute of the first child object
            
            else:
                cmds.warning("Please select more than one mesh")
                
    def readTransform_Children(self, transform_type, transform_axis):
        sel = self.selection()
        object_number = len(sel)
        parent_attr = self.readTransform_Parent(transform_type, transform_axis)
        for i in range(object_number):
            if i < object_number:
                cmds.setAttr(sel[i] + "." + transform_type + transform_axis, parent_attr)

    def matchTranslation(self):
        translate_X = self.readTransform_Children("translate", "X")
        translate_Y = self.readTransform_Children("translate", "Y")
        translate_Z = self.readTransform_Children("translate", "Z")

        return translate_X, translate_Y, translate_Z
    
    def matchRotation(self):
        rotate_X = self.readTransform_Children("rotate", "X")
        rotate_Y = self.readTransform_Children("rotate", "Y")
        rotate_Z = self.readTransform_Children("rotate", "Z")

        return rotate_X, rotate_Y, rotate_Z

    def matchScale(self):
        scale_X = self.readTransform_Children("scale", "X")
        scale_Y = self.readTransform_Children("scale", "Y")
        scale_Z = self.readTransform_Children("scale", "Z")

        return scale_X, scale_Y, scale_Z
    
    def matchAllTransformation(self):
        translate = self.matchTranslation()
        rotate = self.matchRotation()
        scale = self.matchScale()

        return translate, rotate, scale


if __name__ == "__main__":

    try:
        match_transform_dialog.close() # pylint: disable=E0601
        match_transform_dialog.deleteLater()
    except:
        pass

    match_transform_dialog = MatchTransformationPanel()
    match_transform_dialog.show()


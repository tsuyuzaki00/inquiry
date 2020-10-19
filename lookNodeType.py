from mainEdit import qt
from PySide2 import QtWidgets, QtCore, QtGui
import pymel.core as pm

def checkNodeType():
    window = QtWidgets.QWidget(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    layout = QtWidgets.QVBoxLayout(window)

    sels = pm.selected()
    for sel in sels:
        nodeName = sel.nodeType()

        widget = QtWidgets.QLabel(sel + '\t:\t' + nodeName, window)
        layout.addWidget(widget)

    button = QtWidgets.QPushButton('print',window)
    layout.addWidget(button)

    button.clicked.connect(checkNodeType)

    window.show()

def main():
    checkNodeType()
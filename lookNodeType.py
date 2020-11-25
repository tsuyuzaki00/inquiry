from mainEdit import qt
from PySide2 import QtWidgets, QtCore, QtGui
import pymel.core as pm

def checkNodeType():
    window = QtWidgets.QWidget(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    window.resize(350,300)
    layout = QtWidgets.QVBoxLayout(window)

    widget = QtWidgets.QPlainTextEdit(window)

    sels = pm.selected()
    for sel in sels:
        nodeName = sel.nodeType()
        widget.insertPlainText(sel + '\t:\t' + nodeName + '\n')
    
    layout.addWidget(widget)

    button = QtWidgets.QPushButton('print',window)
    layout.addWidget(button)

    button.clicked.connect(main)

    window.show()

def main():
    checkNodeType()
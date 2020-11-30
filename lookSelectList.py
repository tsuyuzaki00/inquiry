from mainEdit import qt
from PySide2 import QtWidgets, QtCore, QtGui
import pymel.core as pm

def selectKeyAttr():
    window = QtWidgets.QWidget(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    window.resize(300,500)
    layout = QtWidgets.QVBoxLayout(window)
    
    widget = QtWidgets.QPlainTextEdit(window)

    sels = pm.selected()

    try:
        widget.insertPlainText(sels[0] + " = [\n")
    except:
        pm.error('Nothing is selected')
    else:
        for sel in sels:    
            widget.insertPlainText("\t'" + sel + "'\n")
        widget.insertPlainText("\t]")
        layout.addWidget(widget)

        button = QtWidgets.QPushButton('print',window)
        layout.addWidget(button)

        button.clicked.connect(main)

        window.show()

def main():
    selectKeyAttr()
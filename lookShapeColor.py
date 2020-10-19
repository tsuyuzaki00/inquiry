from mainEdit import qt
from PySide2 import QtWidgets, QtCore, QtGui
import pymel.core as pm

def checkShapeColor():
    window = QtWidgets.QWidget(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    layout = QtWidgets.QVBoxLayout(window)

    sels = pm.selected()
    for sel in sels:
        shapes = pm.listRelatives(sel[0:], type='nurbsCurve')
        for shape in shapes:
            curveColor = pm.getAttr(shape + '.' + 'overrideColor')

            widget = QtWidgets.QLabel(sel + '\t:\t' + str(curveColor), window)
            layout.addWidget(widget)

            button = QtWidgets.QPushButton('print',window)
            layout.addWidget(button)

            button.clicked.connect(checkShapeColor)

            window.show()

def main():
    checkShapeColor()

main()
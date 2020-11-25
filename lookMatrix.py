from mainEdit import qt
from PySide2 import QtWidgets, QtCore
import pymel.core as pm

def lookMatrix():
    sel = pm.selected()[0]
    normalMatrix = pm.getAttr(sel + ".matrix")
    worldMatrix = pm.getAttr(sel + ".worldMatrix")
    parentMatrix = pm.getAttr(sel + ".parentMatrix")
    xformMatrix = pm.getAttr(sel + ".xformMatrix")
    inverseMatrix = pm.getAttr(sel + ".inverseMatrix")
    worldInverseMatrix = pm.getAttr(sel + ".worldInverseMatrix")
    parentInverseMatrix = pm.getAttr(sel + ".parentInverseMatrix")
    offsetParentMatrix = pm.getAttr(sel + ".offsetParentMatrix")

    window = QtWidgets.QWidget(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    window.resize(400,300)
    layout = QtWidgets.QVBoxLayout(window)
    
    widget = QtWidgets.QPlainTextEdit(window)
    
    matrixLists = [
        ['normalMatrixX', str(normalMatrix[0])],
        ['normalMatrixY', str(normalMatrix[1])],
        ['normalMatrixZ', str(normalMatrix[2])],
        ['normalMatrixT', str(normalMatrix[3])],
        ['worldMatrixX', str(worldMatrix[0])],
        ['worldMatrixY', str(worldMatrix[1])],
        ['worldMatrixZ', str(worldMatrix[2])],
        ['worldMatrixT', str(worldMatrix[3])],
        ['parentMatrixX', str(parentMatrix[0])],
        ['parentMatrixY', str(parentMatrix[1])],
        ['parentMatrixZ', str(parentMatrix[2])],
        ['parentMatrixT', str(parentMatrix[3])],
        ['xformMatrixX', str(xformMatrix[0])],
        ['xformMatrixY', str(xformMatrix[1])],
        ['xformMatrixZ', str(xformMatrix[2])],
        ['xformMatrixT', str(xformMatrix[3])],
        ['inverseMatrixX', str(inverseMatrix[0])],
        ['inverseMatrixY', str(inverseMatrix[1])],
        ['inverseMatrixZ', str(inverseMatrix[2])],
        ['inverseMatrixT', str(inverseMatrix[3])],
        ['inverseWorldMatrixX', str(worldInverseMatrix[0])],
        ['inverseWorldMatrixY', str(worldInverseMatrix[1])],
        ['inverseWorldMatrixZ', str(worldInverseMatrix[2])],
        ['inverseWorldMatrixT', str(worldInverseMatrix[3])],
        ['inverseParentMatrixX', str(parentInverseMatrix[0])],
        ['inverseParentMatrixY', str(parentInverseMatrix[1])],
        ['inverseParentMatrixZ', str(parentInverseMatrix[2])],
        ['inverseParentMatrixT', str(parentInverseMatrix[3])],
        ['offsetParentMatrixX', str(offsetParentMatrix[0])],
        ['offsetParentMatrixY', str(offsetParentMatrix[1])],
        ['offsetParentMatrixZ', str(offsetParentMatrix[2])],
        ['offsetParentMatrixT', str(offsetParentMatrix[3])],
        ]
    for matrixList in matrixLists:
        widget.insertPlainText(matrixList[0] + "\t:\t" + str(matrixList[1]) +"\n")

    layout.addWidget(widget)

    button = QtWidgets.QPushButton('print',window)
    layout.addWidget(button)

    button.clicked.connect(main)

    window.show()

def main():
    lookMatrix()

main()
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

    for sel in sels:
        pm.select(sel)
        selLists = pm.listAttr(k=True)
        for selList in selLists:
            selAttr = pm.getAttr(sel + '.' + selList)
            print "'" + sel + "', '" + selList + "', '" + str(round(selAttr, 3)) + "'"
            widget.insertPlainText("'" + sel + "', '" + selList + "', '" + str(round(selAttr, 3)) + "'"+ "\n")
        widget.insertPlainText("\n")
    layout.addWidget(widget)

    button = QtWidgets.QPushButton('print',window)
    layout.addWidget(button)

    button.clicked.connect(main)

    window.show()

def main():
    selectKeyAttr()
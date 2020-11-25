from mainEdit import qt
from PySide2 import QtWidgets, QtCore, QtGui
import pymel.core as pm
import mainEdit.autoRename as ar

def listBindJoints(sels):
    window = QtWidgets.QWidget(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    window.resize(400,300)
    layout = QtWidgets.QVBoxLayout(window)
    
    widget = QtWidgets.QPlainTextEdit(window)
    
    for sel in sels:
        shape = pm.listRelatives(sel, c = True)
        if shape[0].nodeType() == 'mesh':
            skinCluster = pm.listConnections( shape[0] + '.inMesh', d=False, s=True)
            if skinCluster[0].nodeType() == 'skinCluster':
                bindList = pm.listConnections( skinCluster[0] + '.matrix', d=False, s=True)
                print ar.obj(sel) + 'Bind = ['
                widget.insertPlainText(ar.obj(sel) + 'Bind = [\n')
                for jntList in bindList:
                    print "\t\t'" + jntList + "',"
                    widget.insertPlainText("\t'" + jntList + "',\n")
                print '\t\t]'
                widget.insertPlainText('\t]\n')
                print "\tpm.skinCluster('"+ sel +"', " + ar.obj(sel) + "Bind, tsb = True) "
                widget.insertPlainText("pm.skinCluster('"+ sel +"', " + ar.obj(sel) +"Bind, tsb = True)\n")
            else :
                pm.error('Unbound or SkinCluster is not connected')
        else :
            pm.error('The selected object is not geometry')
    
    layout.addWidget(widget)

    button = QtWidgets.QPushButton('print',window)
    layout.addWidget(button)

    button.clicked.connect(main)
    
    window.show()

def main():
    sels = pm.selected()
    listBindJoints(sels)
from mainEdit import qt
from PySide2 import QtWidgets, QtCore, QtGui
import pymel.core as pm

def listBindJoints():
    sels = pm.selected()

    for sel in sels:
        shape = pm.listRelatives(sel, c = True)
        if shape[0].nodeType() == 'mesh':
            skinCluster = pm.listConnections( shape[0] + '.inMesh', d=False, s=True)
            if skinCluster[0].nodeType() == 'skinCluster':
                bindList = pm.listConnections( skinCluster[0] + '.matrix', d=False, s=True)
                print 'JQPBind = ['
                for jntList in bindList:
                    print "\t\t'" + jntList + "',"
                print '\t\t]'
                print "\tpm.skinCluster('"+ sel +"', JQPBind, tsb = True) "
            else :
                pm.error('Unbound or SkinCluster is not connected')
        else :
            pm.error('The selected object is not geometry')

def main():
    listBindJoints()
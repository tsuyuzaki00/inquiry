from mainEdit import qt
from PySide2 import QtWidgets, QtCore, QtGui
import pymel.core as pm

def selectKeyAttr():
    sels = pm.selected()

    for sel in sels:
        pm.select(sel)
        selLists = pm.listAttr(k=True)
        for selList in selLists:
            selAttr = pm.getAttr(sel + '.' + selList)
            print "'" + sel + "', '" + selList + "', '" + str(selAttr) + "'"

def main():
    selectKeyAttr()
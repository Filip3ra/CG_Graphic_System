import sys

from cProfile import label
from turtle import title
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QGridLayout
from PySide6.QtGui import QFont, QAction
from PySide6.QtCore import Qt



Window_Title = 'TP1'

class MainWindow(QtWidgets.QWidget):
    def __init__(self):     # dunder init?
        super().__init__()  # super?
        self.setWindowWidgetProperties()
        self.MainContainer()
        self.SidePanel()
        


    def setWindowWidgetProperties(self): # OK
        self.setFixedSize(QtCore.QSize(800, 600))
        self.setWindowTitle(Window_Title)

    def MainContainer(self):
        self.mainContainer = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.mainContainer)

    def SidePanel(self): # ainda não está funcionando
        self.SidePanel = QtWidgets.QVBoxLayout()
        self.SidePanel.setAlignment(QtGui.Qt.AlignTop)

        #font = QFont()
        title = QtWidgets.QLabel(Window_Title)
        title.setFont(QFont())
        title.setAlignment(QtGui.Qt.AlignCenter)
        self.SidePanel.addWidget(title)

        self.ObjectManagementGroup()
        self.mainContainer.addLayout(self.SidePanel)

    def ObjectManagementGroup(self): # não funciona ainda
        objectManagementLayout = QtWidgets.QVBoxLayout()

        insertButton = QtWidgets.QPushButton('Insert')
        objectManagementLayout.addWidget(insertButton)

        objectManagementGroup = QtWidgets.QGroupBox('Object Management')
        objectManagementGroup.setLayout(objectManagementLayout)
        self.SidePanel.addWidget(objectManagementGroup)


app = QApplication()
# app.setStyleSheet(load_stylesheet())
window = MainWindow()
window.show()
app.exec()



################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.actionSaveAs = QAction(MainWindow)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionDisplay_Boxes = QAction(MainWindow)
        self.actionDisplay_Boxes.setObjectName(u"actionDisplay_Boxes")
        self.actionDisplay_Boxes.setCheckable(True)
        self.actionDisplay_Indexes = QAction(MainWindow)
        self.actionDisplay_Indexes.setObjectName(u"actionDisplay_Indexes")
        self.actionDisplay_Indexes.setCheckable(True)
        self.actionDisplay_Indexes.setChecked(True)
        self.actionDisplay_Indexes.setEnabled(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 30, 77, 121))
        self.verticalLayout = QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.selected_node = QComboBox(self.horizontalLayoutWidget)
        self.selected_node.setObjectName(u"selected_node")

        self.verticalLayout.addWidget(self.selected_node)

        self.add_button = QPushButton(self.horizontalLayoutWidget)
        self.add_button.setObjectName(u"add_button")

        self.verticalLayout.addWidget(self.add_button)

        self.delete_button = QPushButton(self.horizontalLayoutWidget)
        self.delete_button.setObjectName(u"delete_button")

        self.verticalLayout.addWidget(self.delete_button)

        self.update_button = QPushButton(self.horizontalLayoutWidget)
        self.update_button.setObjectName(u"update_button")

        self.verticalLayout.addWidget(self.update_button)

        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.graph = QGraphicsView(self.centralwidget)
        self.graph.setObjectName(u"graph")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.graph)

        MainWindow.setCentralWidget(self.centralwidget)
        self.graph.raise_()
        self.horizontalLayoutWidget.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuDisplay = QMenu(self.menubar)
        self.menuDisplay.setObjectName(u"menuDisplay")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuDisplay.menuAction())
        self.menu.addAction(self.actionNew)
        self.menu.addAction(self.actionLoad)
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionSaveAs)
        self.menu.addAction(self.actionExport)
        self.menuDisplay.addAction(self.actionDisplay_Boxes)
        self.menuDisplay.addAction(self.actionDisplay_Indexes)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MindMap", None))
        self.actionSaveAs.setText(QCoreApplication.translate("MainWindow", u"Save as ...", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionDisplay_Boxes.setText(QCoreApplication.translate("MainWindow", u"Display Boxes", None))
        self.actionDisplay_Indexes.setText(QCoreApplication.translate("MainWindow", u"Display Indexes", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.update_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuDisplay.setTitle(QCoreApplication.translate("MainWindow", u"Display", None))
    # retranslateUi

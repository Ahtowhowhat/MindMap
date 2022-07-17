
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


# class myQGraphicsView(QGraphicsView):
#     def keyPressEvent(self, event):
#         # 这里event.key（）显示的是按键的编码
#         print("按下：" + str(event.key()))
#         # 举例，这里Qt.Key_A注意虽然字母大写，但按键事件对大小写不敏感
#         # if event.key() == Qt.Key_Escape:
#         #     print('测试：ESC')
#         # elif event.key() == Qt.Key_Down:
#         #     self._updown_button_down('down')
#         #     # your code
#         # elif event.key() == Qt.Key_Up:
#         #     self._updown_button_down('up')
#
#         # 当需要组合键时，要很多种方式，这里举例为“shift+单个按键”，也可以采用shortcut、或者pressSequence的方法。
#         if event.key() == Qt.Key_Left:
#             if QApplication.keyboardModifiers() == Qt.ControlModifier:
#                 print("ctrl + left")
#             else:
#                 print("left")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1350, 790)
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
        self.actionDisplay_Indexes.setChecked(False)
        self.actionDisplay_Indexes.setEnabled(True)
        self.actionFigure_size = QAction(MainWindow)
        self.actionFigure_size.setObjectName(u"actionFigure_size")
        self.actionFont_size = QAction(MainWindow)
        self.actionFont_size.setObjectName(u"actionFont_size")
        self.actionOptimize_position = QAction(MainWindow)
        self.actionOptimize_position.setObjectName(u"actionOptimize_position")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 30, 141, 121))

        # self.horizontalLayoutWidget2 = QWidget(self.centralwidget)
        # self.horizontalLayoutWidget2.setObjectName(u"horizontalLayoutWidget2")
        # self.horizontalLayoutWidget2.setGeometry(QRect(30, 30, 141, 121))

        self.gridLayout = QGridLayout(self.horizontalLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.add_button = QPushButton(self.horizontalLayoutWidget)
        self.add_button.setObjectName(u"add_button")

        self.gridLayout.addWidget(self.add_button, 1, 0, 1, 1)

        self.selected_node = QComboBox(self.horizontalLayoutWidget)
        self.selected_node.setObjectName(u"selected_node")

        self.gridLayout.addWidget(self.selected_node, 0, 0, 1, 1)

        self.update_button = QPushButton(self.horizontalLayoutWidget)
        self.update_button.setObjectName(u"update_button")

        self.gridLayout.addWidget(self.update_button, 3, 0, 1, 1)

        self.delete_button = QPushButton(self.horizontalLayoutWidget)
        self.delete_button.setObjectName(u"delete_button")

        self.gridLayout.addWidget(self.delete_button, 2, 0, 1, 1)

        self.up_button = QPushButton(self.horizontalLayoutWidget)
        self.up_button.setObjectName(u"up_button")

        self.gridLayout.addWidget(self.up_button, 1, 1, 1, 1)

        self.down_button = QPushButton(self.horizontalLayoutWidget)
        self.down_button.setObjectName(u"down_button")

        self.gridLayout.addWidget(self.down_button, 2, 1, 1, 1)

        self.comment_button = QPushButton(self.horizontalLayoutWidget)
        self.comment_button.setObjectName(u"comment_button")

        self.gridLayout.addWidget(self.comment_button, 3, 1, 1, 1)

        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.graph = QGraphicsView(self.centralwidget)
        # self.graph = myQGraphicsView(self.centralwidget)
        self.graph.setObjectName(u"graph")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.graph)

        MainWindow.setCentralWidget(self.centralwidget)
        self.graph.raise_()
        self.horizontalLayoutWidget.raise_()
        # self.pathText.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1350, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuDisplay = QMenu(self.menubar)
        self.menuDisplay.setObjectName(u"menuDisplay")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font = QFont()
        # font.setFamily(u"\u534e\u6587\u7ec6\u9ed1")
        font.setFamily("华文细黑")
        font.setPointSize(14)
        self.statusbar.setFont(font)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuDisplay.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menu.addAction(self.actionNew)
        self.menu.addAction(self.actionLoad)
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionSaveAs)
        self.menu.addAction(self.actionExport)
        self.menuDisplay.addAction(self.actionDisplay_Boxes)
        self.menuDisplay.addAction(self.actionDisplay_Indexes)
        self.menuSettings.addAction(self.actionFigure_size)
        self.menuSettings.addAction(self.actionFont_size)
        self.menuSettings.addAction(self.actionOptimize_position)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MindMap  -by JIE", None))
        self.actionSaveAs.setText(QCoreApplication.translate("MainWindow", u"Save as ...", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionDisplay_Boxes.setText(QCoreApplication.translate("MainWindow", u"Display Boxes", None))
        self.actionDisplay_Indexes.setText(QCoreApplication.translate("MainWindow", u"Display Indexes", None))
        self.actionFigure_size.setText(QCoreApplication.translate("MainWindow", u"Figure size", None))
        self.actionFont_size.setText(QCoreApplication.translate("MainWindow", u"Font size", None))
        self.actionOptimize_position.setText(QCoreApplication.translate("MainWindow", u"Optimize position", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.update_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.up_button.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.down_button.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.comment_button.setText('Comment')
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuDisplay.setTitle(QCoreApplication.translate("MainWindow", u"Display", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

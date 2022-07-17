
################################################################################
## Form generated from reading UI file 'EditWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_editWindow(object):
    def setupUi(self, Ui_editWindow):
        if not Ui_editWindow.objectName():
            Ui_editWindow.setObjectName(u"Ui_editWindow")
        Ui_editWindow.resize(480, 300)
        self.formLayout = QFormLayout(Ui_editWindow)
        self.formLayout.setObjectName(u"formLayout")
        self.commentEdit = QPlainTextEdit(Ui_editWindow)
        self.commentEdit.setObjectName(u"commentEdit")
        font = QFont()
        # font.setFamily(u"\u534e\u6587\u7ec6\u9ed1")
        font.setFamily("华文细黑")
        font.setPointSize(14)
        self.commentEdit.setFont(font)
        self.commentEdit.setPlainText('')

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.commentEdit)

        self.edit_ok_button = QPushButton(Ui_editWindow)
        self.edit_ok_button.setObjectName(u"edit_ok_button")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edit_ok_button)


        self.retranslateUi(Ui_editWindow)

        QMetaObject.connectSlotsByName(Ui_editWindow)
    # setupUi

    def retranslateUi(self, Ui_editWindow):
        Ui_editWindow.setWindowTitle(QCoreApplication.translate("Ui_editWindow", u"Comment", None))
        self.edit_ok_button.setText(QCoreApplication.translate("Ui_editWindow", u"OK", None))
    # retranslateUi


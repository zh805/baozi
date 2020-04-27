# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reset_pic.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_reset(object):
    def setupUi(self, Dialog_reset):
        Dialog_reset.setObjectName("Dialog_reset")
        Dialog_reset.resize(800, 600)
        Dialog_reset.setFixedSize(800, 600)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog_reset)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 320, 361, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog_reset)
        self.commandLinkButton.setGeometry(QtCore.QRect(280, 150, 222, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setIconSize(QtCore.QSize(90, 90))
        self.commandLinkButton.setCheckable(False)
        self.commandLinkButton.setAutoRepeat(False)
        self.commandLinkButton.setAutoRepeatInterval(300)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog_reset)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 390, 361, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.toolButton_3 = QtWidgets.QToolButton(Dialog_reset)
        self.toolButton_3.setGeometry(QtCore.QRect(650, 320, 47, 31))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(Dialog_reset)
        self.toolButton_4.setGeometry(QtCore.QRect(650, 390, 47, 31))
        self.toolButton_4.setObjectName("toolButton_4")
        self.label = QtWidgets.QLabel(Dialog_reset)
        self.label.setGeometry(QtCore.QRect(270, 60, 251, 81))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(Dialog_reset)
        self.label_8.setGeometry(QtCore.QRect(100, 390, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Dialog_reset)
        self.pushButton.setGeometry(QtCore.QRect(320, 450, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(Dialog_reset)
        self.toolButton.setGeometry(QtCore.QRect(590, 320, 47, 31))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(Dialog_reset)
        self.toolButton_2.setGeometry(QtCore.QRect(590, 390, 47, 31))
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_7 = QtWidgets.QLabel(Dialog_reset)
        self.label_7.setGeometry(QtCore.QRect(100, 320, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.layoutWidget = QtWidgets.QWidget(Dialog_reset)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 250, 585, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Dialog_reset)
        QtCore.QMetaObject.connectSlotsByName(Dialog_reset)

    def retranslateUi(self, Dialog_reset):
        _translate = QtCore.QCoreApplication.translate
        Dialog_reset.setWindowTitle(_translate("Dialog_reset", "重置图库"))
        self.label.setText(_translate("Dialog_reset", "重置图库"))
        self.commandLinkButton.setText(_translate("Dialog_reset", "删除旧图库"))

        self.label_4.setText(_translate("Dialog_reset", "菌种名称"))
        self.label_5.setText(_translate("Dialog_reset", "标记名称"))
        self.pushButton_2.setText(_translate("Dialog_reset", "保存"))

        self.label_7.setText(_translate("Dialog_reset", "新图片地址"))
        self.toolButton.setText(_translate("Dialog_reset", "浏览"))
        self.toolButton_3.setText(_translate("Dialog_reset", "添加"))

        self.label_8.setText(_translate("Dialog_reset", "新标记地址"))
        self.toolButton_2.setText(_translate("Dialog_reset", "浏览"))
        self.toolButton_4.setText(_translate("Dialog_reset", "添加"))

        self.pushButton.setText(_translate("Dialog_reset", "生成新图库"))




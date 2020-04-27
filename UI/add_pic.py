# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_pic.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import reset_pic


class Ui_Dialog_add(object):
    def setupUi(self, Dialog_add):
        Dialog_add.setObjectName("Dialog_add")
        Dialog_add.resize(800, 600)
        Dialog_add.setFixedSize(800, 600)
        self.label_8 = QtWidgets.QLabel(Dialog_add)
        self.label_8.setGeometry(QtCore.QRect(120, 490, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog_add)
        self.label_9.setGeometry(QtCore.QRect(110, 340, 661, 16))
        self.label_9.setObjectName("label_9")
        self.reset_bd = QtWidgets.QPushButton(Dialog_add)
        self.reset_bd.setGeometry(QtCore.QRect(570, 110, 93, 31))
        self.reset_bd.setObjectName("reset_bd")
        self.toolButton = QtWidgets.QToolButton(Dialog_add)
        self.toolButton.setGeometry(QtCore.QRect(590, 420, 47, 31))
        self.toolButton.setObjectName("toolButton")
        self.label_4 = QtWidgets.QLabel(Dialog_add)
        self.label_4.setGeometry(QtCore.QRect(290, 250, 60, 28))
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Dialog_add)
        self.label.setGeometry(QtCore.QRect(200, 70, 371, 101))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_add)
        self.label_2.setGeometry(QtCore.QRect(120, 210, 121, 27))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(Dialog_add)
        self.label_6.setGeometry(QtCore.QRect(120, 370, 141, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.toolButton_3 = QtWidgets.QToolButton(Dialog_add)
        self.toolButton_3.setGeometry(QtCore.QRect(650, 420, 47, 31))
        self.toolButton_3.setObjectName("toolButton_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog_add)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 420, 361, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.layoutWidget = QtWidgets.QWidget(Dialog_add)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 280, 531, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.spore_bd = QtWidgets.QPushButton(self.layoutWidget)
        self.spore_bd.setObjectName("spore_bd")
        self.horizontalLayout.addWidget(self.spore_bd)
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog_add)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 490, 361, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.toolButton_2 = QtWidgets.QToolButton(Dialog_add)
        self.toolButton_2.setGeometry(QtCore.QRect(590, 490, 47, 31))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_4 = QtWidgets.QToolButton(Dialog_add)
        self.toolButton_4.setGeometry(QtCore.QRect(650, 490, 47, 31))
        self.toolButton_4.setObjectName("toolButton_4")
        self.comboBox = QtWidgets.QComboBox(Dialog_add)
        self.comboBox.setGeometry(QtCore.QRect(240, 210, 311, 21))
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(Dialog_add)
        self.label_5.setGeometry(QtCore.QRect(440, 250, 60, 28))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Dialog_add)
        self.label_7.setGeometry(QtCore.QRect(120, 420, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog_add)
        QtCore.QMetaObject.connectSlotsByName(Dialog_add)

    def retranslateUi(self, Dialog_add):
        _translate = QtCore.QCoreApplication.translate
        Dialog_add.setWindowTitle(_translate("Dialog_add", "训练数据补充"))

        self.reset_bd.setText(_translate("Dialog_add", "重置图库"))
        self.reset_bd.clicked.connect(self.jump_to_dialog_reset)

        self.label.setText(_translate("Dialog_add", "训练数据补充"))
        self.label_2.setText(_translate("Dialog_add", "已有菌种"))
        
        self.label_3.setText(_translate("Dialog_add", "新添菌种"))
        self.label_4.setText(_translate("Dialog_add", "菌种名称"))
        self.label_5.setText(_translate("Dialog_add", "标记名称"))
        self.spore_bd.setText(_translate("Dialog_add", "添加"))
        
        self.label_9.setText(_translate("Dialog_add", "***************************************************************************"))
        self.label_6.setText(_translate("Dialog_add", "数据补充"))
        
        self.label_7.setText(_translate("Dialog_add", "图片地址"))
        self.toolButton.setText(_translate("Dialog_add", "浏览"))
        self.toolButton_3.setText(_translate("Dialog_add", "添加"))

        self.label_8.setText(_translate("Dialog_add", "标记地址"))
        self.toolButton_2.setText(_translate("Dialog_add", "浏览"))
        self.toolButton_4.setText(_translate("Dialog_add", "添加"))


        

    def jump_to_dialog_reset(self):
        form_reset = QtWidgets.QDialog()
        ui = reset_pic.Ui_Dialog_reset()
        ui.setupUi(form_reset)
        form_reset.show()
        form_reset.exec_()
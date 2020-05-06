# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cover.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import add_pic
import sys



class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 140, 601, 71))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 260, 431, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tuku_bd = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.tuku_bd.setFont(font)
        self.tuku_bd.setObjectName("tuku_bd")
        self.horizontalLayout.addWidget(self.tuku_bd)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.xunlian_bd = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.xunlian_bd.setFont(font)
        self.xunlian_bd.setObjectName("xunlian_bd")
        self.horizontalLayout.addWidget(self.xunlian_bd)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.shibie_bd = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.shibie_bd.setFont(font)
        self.shibie_bd.setObjectName("shibie_bd")
        self.horizontalLayout.addWidget(self.shibie_bd)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(245, 490, 301, 41))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(235, 320, 330, 234))
        # self.label_3.setStyleSheet("image: url(:/image/logo.png);")
        # self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "储粮真菌孢子识别软件"))
        self.label.setText(_translate("mainWindow", "储粮真菌孢子识别软件"))
        self.tuku_bd.setText(_translate("mainWindow", "图库"))
        # self.tuku_bd.clicked.connect(self.jump_to_dialog_add)
        self.xunlian_bd.setText(_translate("mainWindow", "训练"))
        self.shibie_bd.setText(_translate("mainWindow", "识别"))
        self.label_2.setText(_translate("mainWindow", "国家粮食和物资储备局科学研究院"))

    # def jump_to_dialog_add(self):
    #     # self.MainWindow.hide()
    #     form_add = QtWidgets.QDialog()
    #     ui = add_pic.Ui_Dialog_add()
    #     ui.setupUi(form_add)
    #     form_add.show()
    #     form_add.exec_()
    #     # self.MainWindow.show()

    # def exit(self):
    #     self.MainWindow.close()



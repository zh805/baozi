import sys
from PyQt5.QtWidgets import QWidget,QDesktopWidget,QMainWindow,QApplication
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import add
import train
import test


class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin,self).__init__()
        self.initUI()
        self.center()
        self.setTab()

    def initUI(self):
        self.setWindowTitle('真菌孢子识别软件')
        self.resize(800,600)

        # self.status=self.statusBar()
        # self.status.showMessage('',5000)

    def center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        newleft = (screen.width()-size.width())/2
        newtop=(screen.height()-size.height())/2
        self.move(newleft,newtop)

    def setTab(self):
        # 创建界面
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.Layout = QVBoxLayout(self.centralwidget)

        # 设置顶部三个按钮
        self.topwidget = QWidget()
        self.Layout.addWidget(self.topwidget)
        self.buttonLayout = QHBoxLayout(self.topwidget)

        self.pushButton1 = QPushButton()
        self.pushButton1.setText("图库")
        self.buttonLayout.addWidget(self.pushButton1)

        self.pushButton2 = QPushButton()
        self.pushButton2.setText("训练")
        self.buttonLayout.addWidget(self.pushButton2)

        self.pushButton3 = QPushButton()
        self.pushButton3.setText("识别")
        self.buttonLayout.addWidget(self.pushButton3)

        # 设置stackedWidget
        self.stackedWidget = QStackedWidget()
        self.Layout.addWidget(self.stackedWidget)

        self.tuku = QWidget()
        ui1 = add.Ui_Form()
        ui1.setupUi(self.tuku)


        self.xunlian = QDialog()
        ui2 = train.Ui_Form()
        ui2.setupUi(self.xunlian)

        self.shibie = QWidget()
        ui3 = test.Ui_Form()
        ui3.setupUi(self.shibie)

        self.stackedWidget.addWidget(self.tuku)
        self.stackedWidget.addWidget(self.xunlian)
        self.stackedWidget.addWidget(self.shibie)

        self.pushButton1.clicked.connect(self.on_pushButton1_clicked)
        self.pushButton2.clicked.connect(self.on_pushButton2_clicked)
        self.pushButton3.clicked.connect(self.on_pushButton3_clicked)

    # 按钮一：打开第一个面板
    def on_pushButton1_clicked(self):
        self.stackedWidget.setCurrentIndex(0)

    # 按钮二：打开第二个面板
    def on_pushButton2_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    # 按钮三：打开第三个面板
    def on_pushButton3_clicked(self):
        self.stackedWidget.setCurrentIndex(2)



if __name__=='__main__':
    app=QApplication(sys.argv)

    # 应用程序图标
    # app.setWindowIcon(QIcon())

    main=FirstMainWin()
    main.show()

    sys.exit(app.exec_())




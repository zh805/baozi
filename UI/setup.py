from PyQt5 import QtWidgets
from mainWindow import Ui_mainWindow

class mywindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())
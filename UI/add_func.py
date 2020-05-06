import sys
import os
import shutil
import numpy as np

from PyQt5 import QtWidgets
from add import Ui_Form
from PyQt5.QtWidgets import *

class add_win(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(add_win, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.read_folder_pic)
        self.pushButton_4.clicked.connect(self.write_folder_pic)
        self.pushButton_6.clicked.connect(self.read_folder_xml)
        self.pushButton_5.clicked.connect(self.write_folder_xml)

    def read_folder_pic(self):
        filename = QFileDialog.getExistingDirectory(self, "选择图片文件夹","/")
        self.lineEdit_3.setText(filename)

    def read_folder_xml(self):
        filename =  QFileDialog.getExistingDirectory(self, "选择标记文件夹","/")
        self.lineEdit_4.setText(filename)

    def write_folder_pic(self):
        from_path = self.lineEdit_3.text()
        to_path = r'E:\baoziUI\baozi\UI\faster\data\VOCdevkit2007\VOC2007\JPEGImages'

        src_files = os.listdir(from_path)
        for file_name in src_files:
            full_name = os.path.join(from_path, file_name)
            if os.path.isfile(full_name):
                shutil.copy(full_name, to_path)

        jpg_files = os.listdir(to_path)
        name_long = 6
        num_begin = 0
        for i in range(len(jpg_files)):
            file = jpg_files[i]
            if file[-3:] == 'jpg'or file[-3:] == 'bmp':
                img_path = os.path.join(to_path, file)
                b = np.zeros(len(jpg_files)).astype(np.str)
                c = str(i + num_begin)
                ze = name_long - len(c)
                b[i] = '0' * ze + c
                newname = to_path + '/' + b[i] + '.jpg'
                os.rename(img_path, newname)

    def write_folder_xml(self):
        from_path = self.lineEdit_4.text()
        to_path = r'E:\baoziUI\baozi\UI\faster\data\VOCdevkit2007\VOC2007\Annotations'

        src_files = os.listdir(from_path)
        for file_name in src_files:
            full_name = os.path.join(from_path, file_name)
            if os.path.isfile(full_name) and '.xml'in full_name:
                shutil.copy(full_name, to_path)

        xml_files = os.listdir(to_path)
        name_long = 6
        num_begin = 0
        for i in range(len(xml_files)):
            file = xml_files[i]
            if file[-3:] == 'xml':
                xml_path = os.path.join(to_path, file)
                b = np.zeros(len(xml_files)).astype(np.str)
                c = str(i + num_begin)
                ze = name_long - len(c)
                b[i] = '0' * ze + c
                newname = to_path + '/' + b[i] + '.xml'
                os.rename(xml_path, newname)

        txt_path = r'E:\baoziUI\baozi\UI\faster\data\VOCdevkit2007\VOC2007\ImageSets\Main\train.txt'
        f1 = open(txt_path,'w')
        for file_name in os.listdir(to_path):
            f1.write(file_name.rstrip('.xml'))
            f1.write("\n")
        f1.close()


if __name__=='__main__':
    app=QApplication(sys.argv)

    # 应用程序图标
    # app.setWindowIcon(QIcon())

    main=add_win()
    main.show()

    sys.exit(app.exec_())

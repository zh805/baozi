'''
@Time    :   2020/04/25 11:31:00
@Author  :   
@Description: 命令行运行python ui_to_py_tool.py,把UI文件夹中的.ui文件批量转换为.py文件;
'''

import os 
import os.path 

# ui文件所在的相对路径 
dir = './'  

# 列出目录下的所有ui文件
def listUiFile(): 
	list = []
	files = os.listdir(dir)  
	for filename in files:  
		if os.path.splitext(filename)[1] == '.ui':
			list.append(filename)
	
	return list

# 把后缀为ui的文件改成后缀为py的文件名	
def transPyFile(filename): 
	return os.path.splitext(filename)[0] + '.py' 

# 调用系统命令把ui转换成py
def runMain():
	list = listUiFile()
	for uifile in list :
		pyfile = transPyFile(uifile)
		cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile,uifile=uifile)  
		os.system(cmd)

# 程序的主入口
if __name__ == "__main__":  	
	runMain()

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
import tkinter as tk
import sys
from copy import deepcopy

from Task import *
from both_para import *
from Wood import *
from ACO_3fb import *
#import ACO_3fb 

#蚁群参数设置界面
class Ants_Dialog(QDialog):
	def __init__(self,*argv,**kwargs):
		super(Ants_Dialog,self).__init__(*argv,**kwargs)
		self.setWindowTitle('设置蚁群参数')
		self.setWindowIcon(QIcon('../Icon/蚂蚁.png'))
		self.resize(500,200)

		QBtn=QDialogButtonBox.Ok |QDialogButtonBox.Cancel
		self.buttonBox=QDialogButtonBox(QBtn)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)

		#所有的标签和框
		self.ants_label=QLabel("蚂蚁数量:")
		self.ants_edit=QLineEdit()
		self.machines_label=QLabel("机器数量:")
		self.machines_edit=QLineEdit()
		self.top_label=QLabel("上限倍数:")
		self.top_edit=QLineEdit()
		self.iter_label=QLabel("迭代次数:")
		self.iter_edit=QLineEdit()

		self.alpha_label=QLabel("alpha:")
		self.alpha_edit=QLineEdit()
		self.beta_label=QLabel("beta:")
		self.beta_edit=QLineEdit()
		self.thero_label=QLabel("thero(<1.0):")
		self.thero_edit=QLineEdit()
		self.rand_radio=QRadioButton("使用随机规则")
		self.Q_label=QLabel("信息素强度Q")
		self.Q_edit=QLineEdit()

		self.mapping_radio=QRadioButton("对应关系")
		self.mount_radio=QRadioButton("山积图")

		#参数设置组
		self.groupBox_1 = QGroupBox("参数设置")
		layout_1=QVBoxLayout()
		layout_1.addWidget(self.ants_label)
		layout_1.addWidget(self.ants_edit)
		layout_1.addWidget(self.machines_label)
		layout_1.addWidget(self.machines_edit)
		layout_1.addWidget(self.top_label)
		layout_1.addWidget(self.top_edit)
		layout_1.addWidget(self.iter_label)
		layout_1.addWidget(self.iter_edit)
		self.groupBox_1.setLayout(layout_1)

		self.groupBox_2 = QGroupBox("算法参数")
		layout_2=QVBoxLayout()
		layout_2.addWidget(self.alpha_label)
		layout_2.addWidget(self.alpha_edit)
		layout_2.addWidget(self.beta_label)
		layout_2.addWidget(self.beta_edit)
		layout_2.addWidget(self.thero_label)
		layout_2.addWidget(self.thero_edit)
		layout_2.addWidget(self.Q_label)
		layout_2.addWidget(self.Q_edit)
		layout_2.addWidget(self.rand_radio)
		self.groupBox_2.setLayout(layout_2)

		self.groupBox_3 = QGroupBox("输出选项")
		layout_3=QVBoxLayout()
		layout_3.addWidget(self.mapping_radio)
		layout_3.addWidget(self.mount_radio)
		self.groupBox_3.setLayout(layout_3)

		#竖直切割布局，放三个参数框
		self.layout_H=QHBoxLayout()
		self.layout_H.addWidget(self.groupBox_1)
		self.layout_H.addWidget(self.groupBox_2)
		self.layout_H.addWidget(self.groupBox_3)


		self.layout=QVBoxLayout()
		self.layout.addLayout(self.layout_H)
		self.layout.addWidget(self.buttonBox)
		self.setLayout(self.layout)


class Wood_Dialog(QDialog):
	def __init__(self,*argv,**kwargs):
		super(Wood_Dialog,self).__init__(*argv,**kwargs)
		self.setWindowTitle('设置积木参数')
		self.setWindowIcon(QIcon('../Icon/积木(8).png'))
		self.resize(300,200)

		QBtn=QDialogButtonBox.Ok |QDialogButtonBox.Cancel
		self.buttonBox=QDialogButtonBox(QBtn)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)

		
		self.machines_label=QLabel("机器数量")
		self.machines_edit=QLineEdit()
		self.top_label=QLabel("上限倍数")
		self.top_edit=QLineEdit()
		self.iter_label=QLabel("迭代次数")
		self.iter_edit=QLineEdit()
		self.rand_radio=QRadioButton("使用随机规则")
		self.mapping_radio=QRadioButton("对应关系")
		self.mount_radio=QRadioButton("山积图")

		self.groupBox_1 = QGroupBox("参数设置")
		layout_1=QVBoxLayout()
		layout_1.addWidget(self.machines_label)
		layout_1.addWidget(self.machines_edit)
		layout_1.addWidget(self.top_label)
		layout_1.addWidget(self.top_edit)
		layout_1.addWidget(self.iter_label)
		layout_1.addWidget(self.iter_edit)
		self.groupBox_1.setLayout(layout_1)

		self.groupBox_2 = QGroupBox("算法参数")
		layout_2=QVBoxLayout()
		layout_2.addWidget(self.rand_radio)
		self.groupBox_2.setLayout(layout_2)

		self.groupBox_3 = QGroupBox("输出选项")
		layout_3=QVBoxLayout()
		layout_3.addWidget(self.mapping_radio)
		layout_3.addWidget(self.mount_radio)
		self.groupBox_3.setLayout(layout_3)

		#竖直切割布局，放三个参数框
		self.layout_H=QHBoxLayout()
		self.layout_H.addWidget(self.groupBox_1)
		self.layout_H.addWidget(self.groupBox_2)
		self.layout_H.addWidget(self.groupBox_3)


		self.layout=QVBoxLayout()
		self.layout.addLayout(self.layout_H)
		self.layout.addWidget(self.buttonBox)
		self.setLayout(self.layout)

class ShowPhoneNumber_Dialog(QDialog):
	#显示联系我们界面
	def __init__(self,*argv,**kwargs):
		super(ShowPhoneNumber_Dialog,self).__init__(*argv,**kwargs)
		self.setWindowTitle('联系我们')
		self.setWindowIcon(QIcon('../Icon/电话.png'))
		self.resize(200,200)

		self.phone_label=QLabel("电话号码：15709611636")
		self.email_label=QLabel(" 邮  件：Bluffey@163.com")
		self.QQ_label=QLabel(" QQ ：NOT SUPPORT NOW")

		layout_1=QVBoxLayout()
		layout_1.addWidget(self.phone_label)
		layout_1.addWidget(self.email_label)
		layout_1.addWidget(self.QQ_label)
		self.setLayout(layout_1)




class MainWindow(QMainWindow):
	def __init__(self,*args,**kargs):
		super(MainWindow,self).__init__(*args,**kargs)
		#标题
		self.setWindowTitle('U-Line')
		#LOGO
		self.setWindowIcon(QIcon('../ICON/mainIcon.png'))
		self.resize(1100, 600)

		#初始化任务类为空
		self.task=None

		#工具栏：文件拦
		File_toolbar=QToolBar('File_toolbar')
		self.addToolBar(File_toolbar)
		New_action=QAction(QIcon('../ICON/新建.png'),"新建(N)",self)
		Open_action=QAction(QIcon('../ICON/打开.png'),"打开(Open)",self)
		Save_action=QAction(QIcon('../ICON/保存.png'),"保存(S)",self)
		Saveas_action=QAction(QIcon('../ICON/保存(1).png'),"另存为(S)",self)
		Out_action=QAction(QIcon('../ICON/保存(2).png'),"输出(Out)",self)
		New_action.triggered.connect(self.New_clicked)
		Open_action.triggered.connect(self.Open_clicked)
		#Open_action.triggered.connect(self.show_input)
		Save_action.triggered.connect(self.Save_clicked)
		Saveas_action.triggered.connect(self.Saveas_clicked)
		Out_action.triggered.connect(self.Export_clicked)
		File_toolbar.addAction(New_action)
		File_toolbar.addAction(Open_action)
		File_toolbar.addAction(Save_action)
		File_toolbar.addAction(Saveas_action)
		File_toolbar.addAction(Out_action)

		#工具栏:U线工具栏
		U_toolbar=QToolBar('U_toolbar')
		self.addToolBar(U_toolbar)
		U_AS_action=QAction(QIcon('../ICON/u(1).png'),"装配导向型(U-AS)",self)
		U_AU_action=QAction(QIcon('../ICON/u(2).png'),"自动化导向型(U-AU)",self)
		U_UP_action=QAction(QIcon('../ICON/u(3).png'),"无优先关系(U-UP)",self)
		U_CC_action=QAction(QIcon('../ICON/u(4).png'),"复杂约束条件(U-CC)",self)
		L_AS_action=QAction(QIcon('../ICON/L(4).png'),"直线型生产线(L-AS)",self)
		L_AU_action=QAction(QIcon('../ICON/L(5).png'),"直线型生产线(L-AU)",self)
		U_AS_action.triggered.connect(self.U_AS_clicked)
		U_AU_action.triggered.connect(self.U_AU_clicked)
		U_UP_action.triggered.connect(self.U_UP_clicked)
		U_CC_action.triggered.connect(self.U_CC_clicked)
		L_AS_action.triggered.connect(self.L_AS_clicked)
		L_AU_action.triggered.connect(self.L_AU_clicked)
		U_toolbar.addAction(U_AS_action)
		U_toolbar.addAction(U_AU_action)
		U_toolbar.addAction(U_UP_action)
		U_toolbar.addAction(U_CC_action)
		U_toolbar.addAction(L_AS_action)
		U_toolbar.addAction(L_AU_action)

		#编辑拦
		Select_action=QAction(QIcon(),"选择(S)",self)
		Copy_action=QAction(QIcon(),"复制(CP)",self)
		Cut_action=QAction(QIcon(),"剪切(CUT)",self)
		Paste_action=QAction(QIcon(),"粘贴(P)",self)
		Select_action.triggered.connect(self.Select_clicked)
		Copy_action.triggered.connect(self.Copy_clicked)
		Cut_action.triggered.connect(self.Cut_clicked)
		Paste_action.triggered.connect(self.Paste_clicked)

		#设置栏
		Normal_action=QAction(QIcon(),"常规(N)",self)
		Language_action=QAction(QIcon(),"语言(LA)",self)
		Tool_action=QAction(QIcon(),"工具(T)",self)
		#Normal_action.triggered.connect(self.Select_clicked)
		#Language_action.triggered.connect(self.Copy_clicked)
		#Tool_action.triggered.connect(self.Cut_clicked)

		#试图栏：暂时放弃

		#窗口栏：暂时放弃

		#帮助栏
		PDF_action=QAction(QIcon('../ICON/PDF.png'),"软件说明(PDF)",self)
		Contanct_action=QAction(QIcon('../ICON/电话.png'),"联系我们(COT)",self)
		PDF_action.triggered.connect(self.PDF_clicked)
		Contanct_action.triggered.connect(self.Contanct_clicked)

		

		############################
		#菜单栏
		############################
		#文件
		menu=self.menuBar()
		menu.setNativeMenuBar(False)
		File_menu=menu.addMenu("&文件(F)")
		File_menu.addAction(New_action)
		File_menu.addAction(Open_action)
		File_menu.addAction(Save_action)
		File_menu.addAction(Saveas_action)
		File_menu.addAction(Out_action)
		#编辑
		Edit_menu=menu.addMenu("&编辑(E)")
		Edit_menu.addAction(Select_action)
		Edit_menu.addAction(Copy_action)
		Edit_menu.addAction(Cut_action)
		Edit_menu.addAction(Paste_action)
		#设置栏
		Setting_menu=menu.addMenu("&设置(S)")
		Setting_menu.addAction(Normal_action)
		Setting_menu.addAction(Language_action)
		Setting_menu.addAction(Tool_action)

		View_menu=menu.addMenu("&视图(V)")
		#View_menu.addAction(U_AS_action)
		#View_menu.addAction(U_AS_action)
		#View_menu.addAction(U_AS_action)
		#View_menu.addAction(U_AS_action)
		#View_menu.addAction(U_AS_action)
		#View_menu.addAction(U_AS_action)
		#View_menu.addAction(U_AS_action)

		#分析
		Analysis_menu=menu.addMenu("&分析(A)")
		Analysis_menu.addAction(U_AS_action)
		Analysis_menu.addAction(U_AU_action)
		Analysis_menu.addAction(U_UP_action)
		Analysis_menu.addAction(U_CC_action)
		Analysis_menu.addAction(L_AS_action)
		Analysis_menu.addAction(L_AU_action)
		#窗口
		Window_menu=menu.addMenu("&窗口(W)")
		#Window_menu.addAction(U_AS_action)

		#帮助
		Help_menu=menu.addMenu("&帮助(H)")
		Help_menu.addAction(PDF_action)
		Help_menu.addAction(Contanct_action)

		#表格1:任务和时间的对应关系
		self.time_label=QLabel("任务和时间的对应关系:")
		time_header=["任务序号","任务时间"]
		self.time_table=QTableWidget()
		self.time_table.setRowCount(500)            #行数
		self.time_table.setColumnCount(2)           #列数
		self.time_table.setHorizontalHeaderLabels(time_header)

		#表格2:优先级对应关系
		self.predence_label=QLabel("优先级约束关系")
		predence_header=["前向工序","后向工序"]
		self.predence_table=QTableWidget()
		self.predence_table.setRowCount(500)            #行数
		self.predence_table.setColumnCount(2)           #列数
		self.predence_table.setHorizontalHeaderLabels(predence_header)

		#表格3:输出结果
		self.result_label=QLabel("求解结果")
		result_header=["机器序号","机器时间","任务数","任务序号","任务时间","强度"]
		self.result_table=QTableWidget()
		self.result_table.setRowCount(100)            #行数
		self.result_table.setColumnCount(6)           #列数
		self.result_table.setHorizontalHeaderLabels(result_header)


		
		#放第一个表格和标签
		layout_1=QVBoxLayout()
		layout_1.addWidget(self.time_label)
		layout_1.addWidget(self.time_table)

		#放第二个表格和标签
		layout_2=QVBoxLayout()
		layout_2.addWidget(self.predence_label)
		layout_2.addWidget(self.predence_table)

		#放第二个表格和标签
		layout_3=QVBoxLayout()
		layout_3.addWidget(self.result_label)
		layout_3.addWidget(self.result_table)

		#把一和二先放在一起
		layout_half=QHBoxLayout()
		layout_half.addLayout(layout_1)
		layout_half.addLayout(layout_2)

		#放所有表格和标签
		layout_H=QGridLayout()
		#layout_H.setSpacing(10)
		layout_H.addLayout(layout_half,0,0)
		#layout_H.addLayout(layout_2,0,1)
		layout_H.addLayout(layout_3,0,2)
		widget=QWidget()

		widget.setLayout(layout_H)
		self.setCentralWidget(widget)


	def show_input(self):
		#print('run show_input')
		#显示数值
		#显示时间
		for i in range(1,self.task.task_nums+1):
			self.time_table.setItem(i-1,0,QTableWidgetItem(str(i)))
			self.time_table.setItem(i-1,1,QTableWidgetItem(str(self.task.task_time[i])))
		print(len(self.task.precedence[0]))
		for i in range(len(self.task.precedence[0])):
			self.predence_table.setItem(i,0,QTableWidgetItem(str(int(self.task.precedence[0,i]))))
			self.predence_table.setItem(i,1,QTableWidgetItem(str(int(self.task.precedence[1,i]))))

	def show_reslt(self):
		i=1
		while i<=self.para.machine_nums:
			if i==len(self.plan):
				break
			machine=self.plan[str(i)]
			self.result_table.setItem(i-1,0,QTableWidgetItem(str(machine['number'])))
			self.result_table.setItem(i-1,1,QTableWidgetItem(str(float(machine['total_times']))))
			self.result_table.setItem(i-1,2,QTableWidgetItem(str(machine['total_task_nums'])))
			self.result_table.setItem(i-1,3,QTableWidgetItem(str(machine['the_task_number'])))
			self.result_table.setItem(i-1,4,QTableWidgetItem(str(machine['the_task_time'])))
			self.result_table.setItem(i-1,5,QTableWidgetItem(str(machine['total_times']/self.meter*100)+'%'))
			i+=1



	def New_clicked(self):
		#新文件
		pass
	def	Open_clicked(self):
		#新文件
		fileName1,filetype=QFileDialog.getOpenFileName(self,
			"选取文件",
			"C:/",
			"IN2 (*.IN2);;Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔  

		#print(fileName1,filetype)


		#self.setWindowTitle('U-Line:'+str(fileName1))


		df=open(fileName1).readlines()
		task_num=int(df[0])        #获得任务数
		#print(task_num)

		#获得任务时间
		task_time=np.zeros(task_num+1)
		i=1
		while i<task_num+1:
			task_time[i]=int(df[i])
			i+=1


		#获得优先级
		n=df.index('-1,-1\n')
		precedence = np.zeros([2, n-task_num-1])
		while i<n:
			precedence_port=df[i]             #precedence的中间量
			j=precedence_port.index(',')      #j,k在这里的作用是提出优先阵中的分隔符‘，’和‘\’
			k=precedence_port.index('\n')
			precedence[0,i-task_num-1]=int(precedence_port[:j])
			precedence[1,i-task_num-1]=int(precedence_port[j+1:k])
			#print(precedence)
			i+=1


		#赋值并返回
		self.task=Task(task_num,task_time,precedence)
		self.show_input()

	def	Save_clicked(self):
		#
		file_path,filetype =  QFileDialog.getSaveFileName(self,"save file",
			"C:/" ,
			"OUT2 (*.OUT2);;Text Files (*.txt)")
		#print(file_path,type(file_path))

		#plan_out=
		if filetype=="OUT2 (*.OUT2)":
			file_path=file_path+".OUT2"
		elif filetype=="JPEG (*.jpg)":
			file_path=file_path+".jpg"
		#print(file_path,type(file_path))
		outfile = open(file_path, "w")
		out_data=self.plan_to_save()
		#写文件
		outfile.write(out_data)
		#outfile.write(str(self.plan))

	def	Saveas_clicked(self):
		#
		file_path =  QFileDialog.getSaveFileName(self,"save file",
			"C:/" ,
			"OUT2 (*.OUT2);;Text Files (*.txt)")  
		
		if filetype=="OUT2 (*.OUT2)":
			file_path=file_path+".OUT2"
		elif filetype=="JPEG (*.jpg)":
			file_path=file_path+".jpg"
		#print(file_path,type(file_path))
		outfile = open(file_path, "w")
		#写文件
		outfile.write(str(self.plan))

	def	Export_clicked(self):
		#
		file_path =  QFileDialog.getSaveFileName(self,"save file",
			"C:/" ,
			"JPEG (*.jpg);;Text Files (*.png)")

		if filetype=="OUT2 (*.OUT2)":
			file_path=file_path+".OUT2"
		elif filetype=="JPEG (*.jpg)":
			file_path=file_path+".jpg"
		#print(file_path,type(file_path))
		outfile = open(file_path, "w")
		#写文件
		outfile.write(str(self.plan))

	def Select_clicked(self):
		#编辑
		pass
	def	Copy_clicked(self):
		#编辑
		pass
	def	Cut_clicked(self):
		#编辑
		pass
	def	Paste_clicked(self):
		#编辑
		pass
	def U_AS_clicked(self):
		#打开蚁群算法参数设置窗口
		self.U_AS_window=Ants_Dialog(self)
		self.U_AS_window.buttonBox.accepted.connect(self.getUASPara)
		#para.
		self.U_AS_window.exec_()
		pass
	def U_AU_clicked(self):
		#打开积木算法参数设置窗口
		self.U_AU_window=Wood_Dialog(self)
		self.U_AU_window.buttonBox.accepted.connect(self.getUAUPara)
		self.U_AU_window.exec_()
		
	def U_UP_clicked(self):
		#打开蚁群算法参数设置窗口
		pass
	def U_CC_clicked(self):
		#打开蚁群算法参数设置窗口
		pass
	def L_AS_clicked(self):
		#打开蚁群算法参数设置窗口
		pass
	def L_AU_clicked(self):
		#打开蚁群算法参数设置窗口
		pass
	def PDF_clicked(self):
		#显示文档
		pass
	def Contanct_clicked(self):
		#显示电话
		self.contanct_window=ShowPhoneNumber_Dialog(self)
		self.contanct_window.exec_()

		pass
	def getUASPara(self):
		#获得参数
		ant_nums=int(self.U_AS_window.ants_edit.text())
		machine_nums=int(self.U_AS_window.machines_edit.text())
		top=float(self.U_AS_window.top_edit.text())
		ite=int(self.U_AS_window.iter_edit.text())
		alpha=float(self.U_AS_window.alpha_edit.text())
		beta=float(self.U_AS_window.beta_edit.text())
		thero=float(self.U_AS_window.thero_edit.text())
		Q=float(self.U_AS_window.Q_edit.text())
		rand=1#self.U_AS_window.rand_radio.text()


		time_total=self.task.get_timesum()
		time_mean=time_total/machine_nums

		#self.para=WOOD_parameter(ite,machine_nums,time_mean,rand)
		

		self.para=ANTS_parameter(alpha,beta,thero,Q,ite,ant_nums,machine_nums)
		total_times_max=time_mean*top
		self.para.set_top_boder(time_mean*top)
		map_a=initmap(self.task.task_nums,machine_nums)
		#print('map_a=',map_a)
		ants=inital_ant(ant_nums,self.task.task_nums,total_times_max,machine_nums)
		self.plan,self.meter=ANT_STD_ULINE(self.task,ants,map_a,self.para)
		#print('Mainwindow get text is',ants)
		self.show_reslt()

	def getUAUPara(self):
		machine_nums=int(self.U_AU_window.machines_edit.text())
		top=float(self.U_AU_window.top_edit.text())
		ite=int(self.U_AU_window.iter_edit.text())
		#rand=self.U_AU_window.rand_radio.isCheck()
		rand=1

		time_total=self.task.get_timesum()

		time_mean=time_total/machine_nums

		self.para=WOOD_parameter(ite,machine_nums,time_mean,rand)
		self.para.set_top_boder(time_mean*top)

		wood=Wood(self.task.task_nums,machine_nums,self.para.top_boder)
		self.plan,self.meter=STD_WOOD(self.task,self.para,wood)
		self.show_reslt()
		self.draw()

	def plan_to_save(self):
		save_string='{\n'
		for key in self.plan.keys():
			if key=='0':
				pass
			else:
				line=key+':'+str(self.plan[key])+'\n'
				#print(line)
				save_string=save_string+line
		save_string=save_string+'}'
		return save_string


	def draw(self):
		name_list=[]
		num_diffrent=0
		for i in self.plan.keys():
			if i!='0':
				name_list.append("machine"+i)
			if self.plan[i]['total_task_nums']>num_diffrent:
				num_diffrent=self.plan[i]['total_task_nums']

		num_list=[]
		for i in self.plan.keys():
			num_list_i=self.plan[i]['the_task_time']
			len_i=num_diffrent-len(num_list_i)
			if len_i>0:
				for j in range(len_i):
					num_list_i.append(0)
			num_list.append(deepcopy(num_list_i))

		x=np.arange(len(num_list)-1)+1
		data_y=[]
		for i in range(num_diffrent):
			data_y_i=[]
			for j in range(len(num_list)):
				if j!=0:
					data_y_i.append(num_list[j][i])
			data_y.append(data_y_i)
			if i==0:
				plt.bar(x, data_y_i,tick_label=name_list)
			else:
				plt.bar(x, data_y_i,bottom=data_yi1)
			#plt.bar(x, b)
			data_yi1=data_y_i
			#plt.legend()

		print('data_y=\n',data_y)
		plt.show()


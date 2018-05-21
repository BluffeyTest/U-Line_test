import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
import tkinter as tk
import sys
from copy import deepcopy


'''
版本说明：
UI集成版本
该版本是随机扰动版本，且允许集包含前向允许和后向允许。
'''

'''
特别说明一下：
    由于python是从零开始计数的，而实际问题是由1开始计数的，这当中各项关系对应的时候，
转换难免会有一些麻烦，因此，我使用构造0元素的方法来进行计数和计算，即当元素为0时，其
赋值都为0或为空，以保证后续的序号都能对接上。可以将其称为伪任务，伪机器，伪工人，伪
位置等等。


'''

#蚂蚁类
class Ant:
	def __init__(self,task_nums,total_times_max,machine_nums):
		self.task_nums=task_nums
		self.machine_nums=machine_nums
		self.total_times_max=total_times_max
		self.position=np.array([0])
		self.tabu=np.zeros(task_nums+1)-1
		self.machine={'number':0,
		              'total_task_nums':0,
		              'total_times':0,
		              'the_task_number':[],
		              'the_task_time':[]}
		self.plan={}

	'''重设所有非定义时初始化的值，以方便进行新的迭代而不会影响'''
	def re_init(self,meter):
		self.total_times_max=meter
		self.position=np.array([0])
		self.tabu=np.zeros(self.task_nums+1)-1
		self.machine={'number':0,
		              'total_task_nums':0,
		              'total_times':0,
		              'the_task_number':[],
		              'the_task_time':[]}
		self.plan={}

	'''设置当前位置'''
	def position_update(self,position):
		self.position=position
		return self.position

	'''设置当前禁忌表'''
	def set_tabu(self):
		#TODO:设置禁忌表方法
		j=0
		while j<self.task_nums+1:
			if self.tabu[j]==-1:
				#print('position=',self.position)
				self.tabu[j]=self.position
				break
			j=j+1
		#print('tabu=',self.tabu)

	'''或得当前总权重'''
	def get_sum_weight(self,task):
		sum_weight=0
		for position in self.tabu:
			if position==-1:
				break
			else:
				#print('type of position',type(position))
				sum_weight=sum_weight+task.task_time[int(position)]

		return sum_weight

	'''设置当前机器和方案'''
	def machine_update(self,task):
		#先检查零值的情况
		if self.position==0:
			self.plan[str(self.machine['number'])]=deepcopy(self.machine)
			self.machine['number']=self.machine['number']+1
			#print('open a new machine',self.machine['number'])

			#print("machine=",self.machine)
			#print("plan=",self.plan)
			return self.machine,self.plan

		#如果某机器的时间超过最大允许的0.9，则判断添加新任务后会不会超时，超时则添加到下一机器，不超则添加到本机器
		#如果某机器时间未达到最大允许的0.9，则任务添加到本机器
		#如果机器是最后一个机器，则不能打开一个新机器
		if self.machine['number']==self.machine_nums:
			self.machine['total_task_nums']+=1
			self.machine['total_times']+=task.task_time[self.position]
			#self.machine['the_task_number']=
			self.machine['the_task_number'].append(self.position)
			#self.machine['the_task_time']=
			self.machine['the_task_time'].append(task.task_time[self.position])
			'''
		elif self.machine['total_times']>=(self.total_times_max*0.9):
			if (self.machine['total_times']+task.task_time[self.position])>self.total_times_max:
				self.plan[str(self.machine['number'])]=deepcopy(self.machine)
				self.machine['number']=self.machine['number']+1
				print('open a new machine',self.machine['number'])
				self.machine['total_task_nums']=1
				self.machine['total_times']=task.task_time[self.position]
				self.machine['the_task_number']=[self.position]
				self.machine['the_task_time']=[task.task_time[self.position]]
			else:
				self.machine['total_task_nums']+=1
				self.machine['total_times']+=task.task_time[self.position]
				#self.machine['the_task_number']=
				self.machine['the_task_number'].append(self.position)
				#self.machine['the_task_time']=
				self.machine['the_task_time'].append(task.task_time[self.position])
			'''
		elif self.position==0:
			self.plan[str(self.machine['number'])]=deepcopy(self.machine)
			self.machine['number']=self.machine['number']+1
			#print('open a new machine',self.machine['number'])
		elif (self.machine['total_times']+task.task_time[self.position])>self.total_times_max:
			self.plan[str(self.machine['number'])]=deepcopy(self.machine)
			self.machine['number']=self.machine['number']+1
			#print('open a new machine',self.machine['number'])
			self.machine['total_task_nums']=1
			self.machine['total_times']=task.task_time[self.position]
			self.machine['the_task_number']=[self.position]
			self.machine['the_task_time']=[task.task_time[self.position]]
		else:
			self.machine['total_task_nums']+=1
			self.machine['total_times']+=task.task_time[self.position]
			#self.machine['the_task_number']=
			self.machine['the_task_number'].append(self.position)
			#self.machine['the_task_time']=
			self.machine['the_task_time'].append(task.task_time[self.position])

		#如果所有任务已经分配完成，则更新最后一个机器的数据到方案里面
		if (self.position)==self.task_nums:
			self.plan[str(self.machine['number'])]=deepcopy(self.machine)
		self.plan[str(self.machine['number'])]=deepcopy(self.machine)

		#print("machine=",self.machine)
		#print("plan=",self.plan)

		return self.machine,self.plan

	'''计算当前路径索要添加的信息素并返回'''
	def delta_phero(self,task,para):
		if self.position==0:
			delta_T=1
		else:
			delta_T=para.Q*task.task_time[self.position]/np.max(task.task_time)

		return  delta_T

	'''获得选取概率，然后选择相应路径'''
	def chioce(self,task,map_a,allowed_k,para):
		#先取得允许集的最大权重
		weight=[]
		for i in allowed_k:
			weight.append(task.get_time(i))

		#print('weight=',weight)
		max_weight=max(weight)

		#获得地图信息素浓度并求解ng_i
		T=[]
		ng_i=[]
		for i in np.arange(np.size(allowed_k)):
			t=map_a[allowed_k[i],self.machine['number']] #轨迹值
			#print('t=',t)
			T.append(t)
			tt=task.get_time(allowed_k[i])/max_weight #前向权重除以最大权重
			ng_i.append(tt)

		#求和获得一般概率公式的分母
		T=np.array(T)
		#print('T=',T)
		ng_i=np.array(ng_i)
		#print('ng_i=',ng_i)
		den=sum(T**para.alpha*ng_i**para.beta)
		#print('den=',den)
		#求解一般概率矩阵,就是再这儿添加的随机扰动矩阵
		P_ijk=rd.rand((np.size(allowed_k)))*((ng_i**para.alpha)*(T**para.beta))/den
		#求解所要获得的选择的路径
		#方法是取得最大概率的位置，然后该位置所对应的允许集的位置的坐标就是所选的坐标
		m=np.where(P_ijk==np.max(P_ijk))
		#print('m',m,'\nm[0]',m[0])
		if len(m)>1:
			position=allowed_k[m[0][0]]
		elif len(m[0])>1:
			position=allowed_k[m[0][0]]
		else:
			position=allowed_k[m[0]]
		print('position',position)
		#print('type of position',type(position))
		#print('np.max(P_ijk)=',np.max(P_ijk))
		#print('np.where(np.max(P_ijk))=',np.where(np.max(P_ijk)))
		#print('P_ijk=',P_ijk)

		return position,P_ijk

	'''获取当前允许分配的任务集'''
	def get_allowed_k(self,task):
		#挨个所有任务是否在禁忌表里,若不在则放到d里面
		d=[]
		for t in range(task.task_nums+1):
			if (t in self.tabu):
				continue
			elif (t in d):
				continue
			else:
				d.append(t)
		#print('d=',d)


		#可分配任务分为两种，没有前序任务的任务和所有前序任务都分配完成的任务
		#查找所有未分配的后序任务的前序任务是否已经分配完成
		#若是，则将该后序任务写入allowed_k
		#否则，继续下移次循环
		#print('task.precedence[1]=',task.precedence[1])
		#print('list(task.precedence[1])=',list(task.precedence[1]))
		allow_f=[]
		for t in d:
			e=np.where(task.precedence[1]==t)
			#记得改回去
			#if t in list(task.precedence[1]):
				#e.append(list(task.precedence[1]).index(t))
			#print('t=',t)
			#print('e=',e)

			if len(e[0])==0:
				allow_f.append(t)
			else:
				ite=0
				while ite<len(e[0]):
					#print('tt=',tt)
					#print('len(e)=',len(e[0]))
					#print('task.precedence[0,e[0][ite]]=',task.precedence[0,e[0][ite]])
					if (task.precedence[0,e[0][ite]] in self.tabu):
						if (t in allow_f):
							pass
						else:
							allow_f.append(t)
						#print('if:allow=',allow)

					else:
						#if t==1:
							#allow.append(t)
						if (t in allow_f):
							allow_f.remove(t) #删掉t
						#print('else:allow=',allow)
					#print('allow=',allow)
					ite+=1
		allow_b=[]
		for t in d:
			e=np.where(task.precedence[0]==t)
			
			if len(e[0])==0:
				if (t in allow_b):
					continue
				else:
					allow_b.append(t)
			else:
				ite=0
				while ite<len(e[0]):
					#print('tt=',tt)
					#print('len(e)=',len(e[0]))
					#print('task.precedence[0,e[0][ite]]=',task.precedence[0,e[0][ite]])
					if (task.precedence[1,e[0][ite]] in self.tabu):
						if (t in allow_b):
							pass
						else:
							allow_b.append(t)
						#print('if:allow=',allow)

					else:
						#if t==1:
							#allow.append(t)
						if (t in allow_b):
							allow_b.remove(t) #删掉t
						#print('else:allow=',allow)
					#print('allow=',allow)
					ite+=1
		allow=allow_f
		for t in allow_b:
			if t in allow:
				pass
			else:
				allow.append(t)

		allowed_k=np.array(allow)

		print('allowed_k=',allowed_k)
		return allowed_k

	'''输出测试'''
	def out(self):
		print('self.position=',self.position)
		print('self.tabu=',self.tabu)

def inital_ant(num,task_nums,total_times_max,machine_nums):
	'''初始化输入数量的蚂蚁'''

	char=['ant_','=Ant('+str(task_nums)+','+str(total_times_max)+','+str(machine_nums)+')']
	ant_list=[]
	ants_list=[]
	for i in range(num):
		ant_list.append(char[0]+str(i)+char[1])

	#print(ant_list)

	i=0
	while i<num:
		exec(ant_list[i])
		ants_list.append(eval(char[0]+str(i)))
		i=i+1

	#print(ants_list)

	return ants_list


'''初始化地图'''
def initmap(task_nums,machine_nums):
	map_a=np.ones((task_nums+1,machine_nums+1))
	return map_a

'''基本蚁群办法解决生产线问题'''
def ANT_STD_ULINE(task,ants,map_a,para):
	#整个函数就是一堆嵌套循环，直到所有条件满足，输出最佳方案

	#定义全局最佳方案和最佳节拍
	global_min_meter=sys.maxsize
	global_best_plan={}
	#print('map_a in caculate',map_a)
	#最外层，判断是否完成遍历条件
	for ite in np.arange(para.iter):
		print(ite,'次迭代开始')

		#先进行零值的初始赋值，然后才进行实际运算
		delta_phero=np.zeros((task.task_nums+1,para.machine_nums+1))
		delta_map=np.zeros((task.task_nums+1,para.machine_nums+1))
		for k in ants:
			k.position_update(0)                            #将当前位置设为0
			k.set_tabu()                                    #更新禁忌表
			machine,plan=k.machine_update(task)             #更新机器和方案
			#print(machine)
			delta_map=np.zeros((task.task_nums+1,para.machine_nums+1))
			delta_map[machine['number'],0]=k.delta_phero(task,para)
			delta_phero+=delta_map[machine['number'],0]
			                                                #累加所有蚂蚁将要添加的信息素
		map_a=(1-para.thero)*map_a+delta_phero                  #更新全局信息素

		#开始进行实际的路径选择
		t=0
		while t<task.task_nums:
			#print(t,'次选择开始')
			delta_phero=[]
			weight=[]
			for k in ants:
				weight_k=k.get_sum_weight(task)                #获取当前蚂蚁已走路径的总权重
				weight.append(weight_k)                      #将每只蚂蚁已走路径的总权重存起来

			if sum(weight)==0:
				#如果已经走过的路径的总权重为零，则依次选择路径，
				#然后统一更新信息素
				for k in ants:
				    allowed_k=k.get_allowed_k(task)              #获得允许集
				    position,P_ijk=k.chioce(task,map_a,allowed_k,para)  #获得选择位置
				    #print('position=',position)
				    k.position_update(position)                  #更新当前位置
				    k.set_tabu()                         #更新禁忌表
				    machine,plan=k.machine_update(task)          #将当前任务分配给机器并且更新方案
				    delta_map=np.zeros((task.task_nums+1,para.machine_nums+1))
				    											 #每只蚂蚁的时候都清零
				    delta_map[position,machine['number']]=k.delta_phero(task,para)
				                                                 #获得每只蚂蚁所要添加的信息素
				    delta_phero.append(delta_map)                #获得所有蚂蚁所路过的位置所需要添加的信息素的列表
				map_a=(1-para.thero)*map_a+sum(delta_phero)          #更新全局信息素
			else:
				#所有蚂蚁已走过的路径的权重的和不为零
				#则已走路径权重大的蚂蚁有限进行路径选择并更新信息
				#此举意在使路径短的蚂蚁能够影响到路径长的蚂蚁的选择
				map_a=(1-para.thero)*map_a                               #先蒸发后读取
				ii=0
				while ii<len(weight):
					if max(weight)!=-1:
						p=weight.index(max(weight))                      #找到最大权重第一次出现的地方
						k=ants[p]                                        #该位置对应的蚂蚁
						weight[p]=-1                                     #将最大值改为最小值

						#进行常规的选择操作
						allowed_k=k.get_allowed_k(task)   
						#print('allowed_k=',allowed_k)           #获得允许集
						position,P_ijk=k.chioce(task,map_a,allowed_k,para)  #获得选择位置
						#print('position=',position)
						k.position_update(position)                  #更新当前位置
						k.set_tabu()                         #更新禁忌表
						machine,plan=k.machine_update(task) 
						#print('machine=',machine)         #将当前任务分配给机器并且更新方案
						#print('plan=',plan)
						delta_map=np.zeros((task.task_nums+1,para.machine_nums+1))      #每只蚂蚁的时候都清零
						delta_map[position,machine['number']]=k.delta_phero(task,para)  #获得每只蚂蚁所要添加的信息素
						map_a=map_a+delta_map                        #进行单个蚂蚁的信息素的更新,这样先进性选择的蚂蚁的信息素就可以影响到后选择的蚂蚁的选择
				    #else:
				    	#基本不会有希望用到这个else，但还是保险起见，让他跳出循环
				    	#break

					ii+=1
			#print(t,'次选择结束')
			t+=1

		#每只蚂蚁都遍历完成后，提取出最佳方案
		#最佳方案的标准是平衡率最大，即节拍最小
		plans=[]
		meter=[]                              #表示节拍
		for k in ants:
			plans.append(deepcopy(k.plan))
			#print('plan=',plan)

			#取得单个plan的节拍
			meter_port=0
			for key in k.plan.keys():
				#print('k.key=',k,key)
				#print("k.plan[key]['total_times']",k.plan[key]['total_times'])

				if k.plan[key]['total_times']>meter_port:
					meter_port=k.plan[key]['total_times']
					#print('meter_port=',meter_port)
				else:
					pass

			meter.append(meter_port)

		#print('plan=',plan)
		print('meter=',meter)
		#获得此次遍历的最佳方案
		min_meter=min(meter)
		index=meter.index(min_meter)
		#print('index=',index)
		#print('plans[index]=',plans[index])
		part_best_plan=deepcopy(plans[index])
		#print('part_best_plan=',part_best_plan)


		#获得当前全局最佳方案
		if global_min_meter>min_meter:
			global_min_meter=min_meter
			global_best_plan=deepcopy(part_best_plan)
		else:
			pass


		#现完成单次遍历完成后，还需进行多次遍历的计算
		#因此，在此处对每只蚂蚁再进行重初始化
		#重初始化不会影响到蚂蚁最开始对蚂蚁进行初始化定义时的值
		for k in ants:
			k.re_init(global_min_meter-1)

		print(ite,'次迭代结束')


	#所有遍历次数都结束后，输出最佳方案，及其节拍
	return global_best_plan,global_min_meter

def check_mean_and_max(task,machine_nums):
	pass








#####################################################################
##    以下是主程序              
#####################################################################
def test():
		
	#task=get_task('F:\毕业论文\数据\SALBP-data-sets\precedence graphs\ARC83.IN2')
	task=get_task()
	#task.out()
	ant_num=10
	machine_nums=int(input('please input the machine numbers:'))
	#para=parameter(alpha,beta,thero,Q,max_iter,machine_nums)
	para=parameter(0.6,0.6,0.8,0.5,200,machine_nums)

	#print(type(machine_nums))
	total_times_max=np.sum(task.task_time)/machine_nums*1.05
	#check_mean_and_max();
	#print('sum of task.task_time=',np.sum(task.task_time))
	#print('total_times_max=',total_times_max)
	ants=inital_ant(ant_num,task.task_nums,total_times_max,machine_nums)
	#print(type(ants[0]))
	#ants[0].out()

	map_a=initmap(task.task_nums,machine_nums)
	plan,meter=ANT_STD_ULINE(task,ants,map_a,para)
	#print('plan=',plan)
	#print('meter=',meter)
	s=0
	s_t=0
	for key in plan:
		s+=plan[key]['total_times']
		print(key,plan[key]['total_times'])
		print(plan[key]['the_task_number'])
		s_t+=plan[key]['total_task_nums']
	print('s=',s)
	print('s_t=',s_t)
	print('meter=',meter)

	#print('total_times_max=',total_times_max)





import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
import tkinter as tk
import sys
from copy import deepcopy


'''
版本说明：积木模型UI集成版本
'''



class Wood:
	def __init__(self,task_nums,machine_nums,top_boder):
		self.task_nums=task_nums
		self.machine_nums=machine_nums
		self.top_boder=top_boder
		self.wood=np.array([0])
		self.tabu=np.zeros(task_nums+1)-1
		self.space={'number':0,
		            'total_task_nums':0,
		            'total_times':0,
		            'the_task_number':[],
		            'the_task_time':[]}
		self.plan={}

	'''设置禁忌表'''
	def set_tabu(self):
		#TODO:设置禁忌表方法
		j=0
		while j<self.task_nums+1:
			if self.tabu[j]==-1:
				self.tabu[j]=self.wood
				break
			j=j+1
		#print('tabu=',self.tabu)

	'''设置当前小积木块'''
	def wood_update(self,wood):
		self.wood=int(np.array(wood))
		return self.wood

	'''常规选择方式,不涉及到随机捆绑'''
	def chioce(self,allowed_k,task,para):

		#取得允许集对应的时间
		time=[]
		for i in allowed_k:
			time.append(task.get_time(i))
		#print('time=',time)

		P=[]
		if self.top_boder==0:
			#当上界为初始上界的时候，执行概率计算
			for i in range(len(time)):
				P.append(1+np.log((self.space['total_times']+time[i])/para.time_mean))
				if P[i]<0 and (para.rand):
					#print('run if if')
					P[i]=rd.rand(1)
					P[i]=[0]
					print(P[i])
				else:
					#print('run if else')
					P[i]=[0]
					print(P[i])
		else:
			#当上界为确定上界的时候，超过均值的部分采用线性下降
			for i in range(len(time)):
				time_total=self.space['total_times']+time[i]
				if time_total>para.time_mean:
					#大于上界就把概率改为-1
					#print('run else if',para.time_mean,self.top_boder)
					if time_total>self.top_boder:
						P.append(-1)
					else:
						#print('time_total',time_total)
						P.append((time_total-para.time_mean)/(self.top_boder-para.time_mean))
				else:
					#print('run else else')
					P.append(1+np.log((self.space['total_times']+time[i])/para.time_mean))
					if P[i]<0 and (para.rand):
						#此处有问题，待修改
						P[i]=rd.rand(1)
					else:
						P[i]=0

		#print('P',P)
		P_ij=np.array(P)
		#print('1,P_ij',P_ij)

		#如果全部都超过上界的话就只能分配给下一个槽了，
		#但是此处不做槽的更新，只能将该信息传出去，并重新计算概率		
		new_space=0
		if np.max(P_ij)==-1:
			#print('re caculate')
			new_space=1
			P=[]
			for i in range(len(time)):
				time_total=time[i]
				if time_total>para.time_mean:
					#大于上界就把概率改为-1
					if time_total>para.top_boder:
						P.append([-1])
					else:
						P.append((time_total-para.time_mean)/(self.top_boder-para.time_mean))
				else:
					P.append(1+np.log(time[i]/para.time_mean))
					if P[i]<0 and (~para.rand):
						P[i]=[0]
					else:
						P[i]=rd.rand(1)
		P_ij=np.array(P)
		#print('P_ij',P_ij)
		#print('max_position',np.where(P_ij==np.max(P_ij)))
		m=np.where(P_ij==np.max(P_ij))
		#print('m',m,'\nm[0]',m[0])
		if len(m)>1:
			wood=allowed_k[m[0][0]]
		elif len(m[0])>1:
			wood=allowed_k[m[0][0]]
		else:
			wood=allowed_k[m[0]]


		return wood,P_ij,new_space

	'''更新积木槽'''	
	def space_update(self,task,new_space):
		#先检查零值的情况
		if self.wood==0:
			self.plan[str(self.space['number'])]=deepcopy(self.space)
			self.space['number']=self.space['number']+1
			#print('open a new space',self.space['number'])

			#print("space=",self.space)
			#print("plan=",self.plan)
			return self.space,self.plan
		if self.space['number']==self.machine_nums:
			self.space['total_task_nums']+=1
			self.space['total_times']+=task.task_time[self.wood]
			self.space['the_task_number'].append(self.wood)
			self.space['the_task_time'].append(float(np.array(task.task_time[self.wood])))
		elif new_space==1:
			self.plan[str(self.space['number'])]=deepcopy(self.space)
			self.space['number']=self.space['number']+1
			print('open a new space',self.space['number'])
			self.space['total_task_nums']=1
			self.space['total_times']=task.task_time[self.wood]
			self.space['the_task_number']=[self.wood]
			self.space['the_task_time']=[float(np.array(task.task_time[self.wood]))]
		else:
			self.space['total_task_nums']+=1
			self.space['total_times']+=task.task_time[self.wood]
			self.space['the_task_number'].append(self.wood)
			self.space['the_task_time'].append(float(np.array(task.task_time[self.wood])))

		self.plan[str(self.space['number'])]=deepcopy(self.space)
		return self.space,self.plan

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
		#print('allowed_k=',allow)
		return allowed_k

	'''重设所有非定义时初始化的值，以方便进行新的迭代而不会影响'''
	def re_init(self,meter):
		self.top_boder=meter
		self.position=np.array([0])
		self.tabu=np.zeros(self.task_nums+1)-1
		self.space={'number':0,
		              'total_task_nums':0,
		              'total_times':0,
		              'the_task_number':[],
		              'the_task_time':[]}
		self.plan={}


'''初始化地图'''
def initmap(task_nums,machine_nums):
	map_a=np.ones((task_nums+1,machine_nums+1))
	return map_a


def STD_WOOD(task,para,wood):
	#定义全局最佳方案和最佳节拍
	global_min_meter=sys.maxsize
	global_best_plan={}

	#最外层，判断是否完成遍历条件
	for ite in np.arange(para.iter):
		print(ite,'次迭代开始')
		i=0
		part_meter=0
		while i<=task.task_nums:
			if i==0:
				wood.wood_update(0)                            #将当前位置设为0
				wood.set_tabu()                                    #更新禁忌表
				machine,plan=wood.space_update(task,1)
				i+=1
				continue 
			#print(i,'次选择开始')
			allowed_k=wood.get_allowed_k(task)
			#print('allowed_k=',allowed_k)
			wood_i,P_ij,new_space=wood.chioce(allowed_k,task,para)
			#print('wood_i',wood_i)
			#print('P_ij=',P_ij)
			#print('new_space=',new_space)
			wood.wood_update(wood_i)
			wood.set_tabu()
			space,plan=wood.space_update(task,new_space)
			#print('plan',plan)
			#print('space',space)
			#print(i,'次选择结束')
			i+=1
		#更新上界和清空槽和禁忌表
		for key in plan.keys():
			if plan[key]['total_times']>part_meter:
				part_meter=plan[key]['total_times']

		if global_min_meter>part_meter:
			global_min_meter=part_meter
			global_best_plan=deepcopy(plan)

		wood.re_init(global_min_meter-1)


		print(ite,'次迭代结束')


	#所有遍历次数都结束后，输出最佳方案，及其节拍
	return global_best_plan,global_min_meter



def test():
	task=get_task()
	print('task_time',task.task_time)
	machine_nums=int(input('please input the machine numbers:'))
	time_mean=task.get_timesum()/machine_nums
	#para=parameter(max_ite,machine_nums,time_mean,rand)
	para=parameter(100,machine_nums,time_mean,1)
	top_boder=1.02*time_mean
	wood=Wood(task.task_nums,machine_nums,top_boder)
	plan,meter=STD_WOOD(task,para,wood)
	print('plan=',plan)
	print('meter=',meter)


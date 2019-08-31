import numpy as np 
#纯粹的就是任务的类
class Task:
	'''
	任务矩阵，包含基本的任务数矩阵，任务时间矩阵，任务优先级矩阵
	'''
	def __init__(self, task_nums, task_time, precedence):
		self.task_nums=task_nums
		self.task_time=task_time
		self.precedence=precedence

	def out(self):
		'''输出task'''
		print('task_nums=',self.task_nums)
		print('task_time=', self.task_time)
		print('precedence=', self.precedence)
	def get_time(self,i):
		return self.task_time[i]
	def get_timesum(self):
		return np.sum(self.task_time)
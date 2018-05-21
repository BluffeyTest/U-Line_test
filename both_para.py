

'''
用于UI的蚁群算法和积木模型的参数设置
'''

# 通过输入进行定义的参数列表
# alpha：蚁群算法的参数alpha
# beta ：蚁群算法的参数beta
# thero：蚁群算法的参数thero
# Q    ：信息素强度
# max_iter:
#        迭代次数，即需要完成的遍历次数
class ANTS_parameter:
	def __init__(self,alpha,beta,thero,Q,max_iter,ants,machine_nums):
		self.alpha=alpha
		self.beta=beta
		self.thero=thero
		self.Q=Q
		self.iter=max_iter
		self.ants=ants
		self.machine_nums=machine_nums
		self.mapping=1
		self.mount=0
	def set_top_boder(self,top_boder):
		'''设置上界'''
		self.top_boder=top_boder

# 通过输入进行定义的参数列表
# machine_nums:机器数量
#time_mean：平均时间
#rand：是否使用随机规则增加适应性
# Q    ：信息素强度
# max_iter:
#        迭代次数，即需要完成的遍历次数
class WOOD_parameter:
	def __init__(self,max_iter,machine_nums,time_mean,rand):
		self.iter=max_iter
		self.machine_nums=machine_nums
		self.top_boder=0
		self.time_mean=time_mean
		self.rand=rand
		self.mapping=1
		self.mount=0
	def set_top_boder(self,top_boder):
		'''设置上界'''
		self.top_boder=top_boder


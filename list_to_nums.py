import numpy as np

def list_to_int(list):
	L=[]
	i=0
	while i<len(list):
		L.append(int(str(list[i])))
		i+=1

	return L

def list_to_float(list):
	L=[]
	i=0
	while i<len(list):
		L.append(float(list[i]))
		i+=1

	return L


def test():
	#a=np.arange(9)
	a=[3,[4],5]
	print('a=',a)
	b=list_to_int(a)
	print('b=',b)
	c=np.array(b)
	print('c=',c)

#test()
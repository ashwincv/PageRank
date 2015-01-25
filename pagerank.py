import random

alpha = 0.85
input_file = open("hw2-sample-input",'r')
nodes = int(input_file.read(1))
space = input_file.read(1)
edges = int(input_file.read(1))
graph = {}
#print nodes
#print space
#print edges

adj_list = {}
pagerank = []


for i in range(nodes+1):
	temp = 10 
	pagerank.append(float(temp)/100) 
	 

input_file.readline()



for j in range(edges):
	temp = input_file.readline()
	if int(temp[0]) not in adj_list.keys():
		temp_list = []
		temp_list.append(int(temp[2]))
		adj_list[int(temp[0])] = temp_list
	else:
		#print adj_list[int(temp[0])]
		temp_list = adj_list[int(temp[0])]
		temp_list.append(int(temp[2])) 
		adj_list[int(temp[0])] = temp_list


'''
for k in range(1,nodes+1):
	if k not in adj_list.keys():
		temp_list = []
		for a in range(1,nodes+1):
			if a!=k:
				temp_list.append(int(a))
		adj_list[int(k)] = temp_list
'''		


#print adj_list[1]
#print pagerank
#print len(adj_list
check = 0
#while check<=nodes:
for count in range(10):
		for v in range(1,int(nodes)+1):
			#print v
			pagerank[v] = float(1- alpha)/int(nodes)
			for g in range(1,int(nodes)+1):
				
				if g in adj_list.keys():
					print g
					for k in adj_list[g]:
						if k ==v:
							pagerank[v]+=(alpha*(pagerank[g]/len(adj_list[g])))

			
print pagerank 

#print input_file.readline()



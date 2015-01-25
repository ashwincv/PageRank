import random
import sys

''' @inputf = input file 
	@outputf = output file
'''
inputf = sys.argv[1]
outputf = sys.argv[2]





'''
	@alpha = damping coefficient
'''
alpha = 0.85







''' 
	Open input file for reading(provided in the same directory)
'''
input_file = open("hw2-sample-input",'r')






'''
	Read the first line to get number of edges and nodes
	@nodes = number of nodes
	@edges = number of edges
	@space = variable to be discarded, takes the space character
'''
nodes = int(input_file.read(1))
space = input_file.read(1)
edges = int(input_file.read(1))






'''
	@adj_list = Dictionary that stores {node (key) : list of nodes with incoming edges to this node (value)}
	@pagerank = List which stores PageRank values
	@out      = List to count number of outgoing edges from each node
'''
adj_list = {}
pagerank = []
out = []






'''
	Initialize PageRank's of all the nodes to (1/N)
'''
for i in range(1,nodes+1):
	temp = float(1)/float(nodes)
	pagerank.append(temp) 
	 

#Buffer Line
input_file.readline()


'''
	Reading in all the edges and storing them in @adj_list
	@temp = temporary variable to store current line to be parsed
	@temp_list = temporary list to store list that is going to be modified
'''
for j in range(edges):
	temp = input_file.readline()
	out.append(int(temp[0]))
	if int(temp[2]) not in adj_list.keys():
		temp_list = []
		temp_list.append(int(temp[0]))
		adj_list[int(temp[2])] = temp_list
	else:
		temp_list = adj_list[int(temp[2])]
		temp_list.append(int(temp[0])) 
		adj_list[int(temp[2])] = temp_list


'''
	Removing repetitions
'''
out_list = set(out)





'''
	Setting outdegree of sink nodes to n-1
'''
check = 0
for a in range(1, nodes+1):
	check = 0
	for b in out_list:
		if int(a) == int(b):
			check+=1

	if check==0:
			for k in range(1,nodes+1):
				if(k!=a):
					if k not in adj_list.keys():
						temp_list = []
						temp_list.append(int(a))
						adj_list[int(k)] = temp_list
					else:
						temp_list = adj_list[int(k)]
						temp_list.append(int(a)) 
						adj_list[int(k)] = temp_list

	



'''
	Calculating number of outbound links from every node
'''
outbound_links = [0 for a in range(1,nodes+1)]

for a in adj_list.keys():
	for b in adj_list[a]:
		outbound_links[b-1]+=1



'''
	Calculating PageRank
'''
check = 0
while check<=2:
		temp1 = pagerank[0]     											#To check for convergence
		for v in range(1,int(nodes)+1):
			pagerank[v-1] = float(1- alpha)/int(nodes)						#Constant Factor
			for g in adj_list[v]:
				pagerank[v-1]+=(alpha*(pagerank[g-1]/outbound_links[g-1]))
		print round(pagerank[0],5),round(temp1,5)
		if round(pagerank[0],12)==round(temp1,12):                           #Checking if values have converged
			check+=1
		


'''
	Writing in output file
'''
output = open("output.txt",'w')

for a in pagerank:
	output.write(str(a)+"\n")

output.close()


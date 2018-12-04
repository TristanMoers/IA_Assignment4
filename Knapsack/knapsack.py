#! /usr/bin/env python3
'''NAMES OF THE AUTHOR(S): Gaël Aglin <gael.aglin@uclouvain.be>, Francois Aubry <francois.aubry@uclouvain.be>'''
from search import *
import re
import sys


class Knapsack(Problem):

	def __init__(self,initFile):
		try:
			file=open(initFile,'r')
			self.nItems = int(file.readline().strip().rstrip('\n'))
			self.itemWeight = []
			self.itemUtil = []
			self.conflicts = []

			for i in range(self.nItems):
				data = file.readline().strip().rstrip('\n')
				data = re.sub(' +',' ',data).split(' ')
				self.itemWeight.append(int(data[1]))
				self.itemUtil.append(int(data[2]))
				if len(data) > 3:
					self.conflicts.append([int(w)-1 for w in data[3:]])
				else:
					self.conflicts.append([])

			self.capacity = int(file.readline().strip().rstrip('\n'))
			file.close()

			self.initial = self.initial_state()

		except IOError as error:
			print('Error opening the instance file: '+str(error))
			exit(-1)

	def initial_state(self):
		pass

	def successor(self,state):
		pass

	def getUtility(self,state):
		"""
		:param state:
		:return: utility of the state in parameter
		"""
		return 0

	def __str__(self):
		s=str(self.nItems)+'\n'
		for i in range(self.nItems):
			s+= '\t'+str(i)+' '+str(self.itemWeight[i])+' '+str(self.itemUtil[i])+'\n'
		s+= str(self.capacity)
		return s


#################
# Local Search #
#################

def maxvalue(problem, limit=100, callback=None):
    current = LSNode(problem, problem.initial, 0)
    best = current
    # Put your code here!

    return best


def randomized_maxvalue(problem, limit=100, callback=None):
    current = LSNode(problem, problem.initial, 0)
    best = current
    # Put your code here!

    return best




#####################
#       Launch      #
#####################

if(len(sys.argv) <=2 ):
	print("Usage: "+sys.argv[0]+" instance_file technique_value (0: randomWalk,1: maxValue,2: randomizedMaxvalue)")
	exit(-1)

knap = Knapsack(sys.argv[1])

stepLimit = 100

tech = int(sys.argv[2])

if(tech == 0):
	node = random_walk(knap,stepLimit)
elif(tech == 1):
	node = maxvalue(knap,stepLimit)
elif(tech == 2):
	node = randomized_maxvalue(knap,stepLimit)


state = node.state
print("weight: " + str(state[2]) + " utility: " + str(state[3]))
print("Items: " + str([x for x in state[0]]))
print("Capacity: " + str(knap.capacity))
print("STEP: "+str(node.step))
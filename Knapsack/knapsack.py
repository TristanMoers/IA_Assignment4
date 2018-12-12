#! /usr/bin/env python3
'''NAMES OF THE AUTHOR(S): GaÃ«l Aglin <gael.aglin@uclouvain.be>, Francois Aubry <francois.aubry@uclouvain.be>'''
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
		new_list = list()
		return State(0, new_list, 0)

	def successor(self,state):
		tab = []
		if state.path == []:
			for i in range(1, self.nItems+1):
				path = state.path.copy()
				path.append(i)
				new_state = State(self.itemWeight[i-1], path, self.itemUtil[i-1])
				#yield ('move', new_state)
				tab.append(('move', new_state))
		else:
			for i in range(1, self.nItems+1):
				if not self.check_in_path(state.path, i) and not self.check_conflict(state.path, i) and self.check_weight(state.actual_weight + self.itemWeight[i-1]):
					path = state.path.copy()
					path.append(i)
					new_state = State(state.actual_weight + self.itemWeight[i-1], path, state.actual_utility + self.itemUtil[i-1])
					#yield ('move', new_state)
					tab.append(('move', new_state))
		for i in tab:
			yield i

	def check_conflict(self, path, elem):
		for i in path:
			if elem-1 in self.conflicts[i-1]:
				return True
		return False

	def check_in_path(self, path, elem):
		return elem in path

	def check_weight(self, weight):
		return weight <= self.capacity

	def value(self,state):
		"""
		:param state:
		:return: utility of the state in parameter
		"""
		if state.actual_utility == 0:
			return 0
		else:
			return state.actual_weight / state.actual_utility

	def __str__(self):
		s=str(self.nItems)+'\n'
		for i in range(self.nItems):
			s+= '\t'+str(i)+' '+str(self.itemWeight[i])+' '+str(self.itemUtil[i])+'\n'
		s+= str(self.capacity)
		return s


#################
# Local Search #
#################

class State():

	def __init__(self, actual_weight, path, actual_utility):
		self.actual_weight = actual_weight
		self.path = path
		self.actual_utility = actual_utility


def maxvalue(problem, limit=100, callback=None):
	current = LSNode(problem, problem.initial, 0)
	best = current
	for step in range(limit):
		if callback is not None:
			callback(current)
		successors = list(current.expand())
		if successors != []:
			current = min(successors, key=lambda x: x.problem.value(x.state))
		else:
			break
		if current.value() > best.value():
			best = current
	return best


def randomized_maxvalue(problem, limit=100, callback=None):
	current = LSNode(problem, problem.initial, 0)
	best = current
	for step in range(limit):
		if callback is not None:
			callback(current)
		successors = list(current.expand())
		if successors != []:
			successors = sorted(successors, key=lambda x: x.problem.value(x.state))
			current = random.choice(successors[0:5])			
		else:
			break
		if current.value() > best.value():
			best = current
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
print("weight: " + str(state.actual_weight) + " utility: " + str(state.actual_utility))
print("Items: " + str([x for x in state.path]))
print("Capacity: " + str(knap.capacity))
print("STEP: "+str(node.step))

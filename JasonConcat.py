import json
import csv
import os
from os import path
import time
import gc
from ctypes import util, cdll
import ast
import sys

cwd = os.getcwd()

def mergesjson(Finalpath, NodePath):

	FinalNodesNames = [] 
	FlagFound = 0;
	FlagFinalEmpty = 0
	FlagAddEmpty = 0

	with open(Finalpath,'r') as Finaljsonfile:
	    try:
	    	FinalNodes = json.load(Finaljsonfile)
	    	for key in FinalNodes.keys():
	    		FinalNodesNames.append(key) #getting the name of the rows (Node1,Node2,Node3...etc)
	    except:
	    	FlagFinalEmpty = 1 #Checks If the Final Path is Empty

	with open(NodePath,'r') as AddingNodejsonfile:
	    try:
		    AddNodes = json.load(AddingNodejsonfile)
		    for key in AddNodes.keys():
		    	AddNodesName = key
	    except:
	    	FlagAddEmpty = 1 #Checks If Adding Path is Empty or not

	if FlagFinalEmpty == 0 and FlagAddEmpty == 0:
		for NodeNames in FinalNodesNames:
			if AddNodesName == NodeNames: # Checks if the node is in it already or not
				FlagFound = 1
				break
			else:
				FlagFound = 2


	if FlagFound == 0: # That mean Either FlagAddEmpty = 1 or FlagFinalEmpty = 1 or both
		if FlagFinalEmpty == 0 and FlagAddEmpty == 1:
			FinalNodes = FinalNodes;
		elif FlagFinalEmpty == 1 and FlagAddEmpty == 0:
			FinalNodes = AddNodes;
		else:
			print('Both Are Empty')
			exit()

	elif FlagFound == 1:
		AddNodes = str(AddNodes)
		AddNodes = AddNodes.rsplit('}',2)[0]
		AddNodes = AddNodes.split('{',2)[2]
		AddNodes = ast.literal_eval('{' + AddNodes +'}')
		for tmpkey in AddNodes.keys():
			FinalNodes[AddNodesName][0][tmpkey] = AddNodes[tmpkey]

	else: #If it doesn't find it it will just Add the entire node in to the dictonary
		FinalNodes[AddNodesName] = AddNodes[AddNodesName]

	with open(Finalpath, 'w') as outfile:
		json.dump(FinalNodes, outfile) # Dumping back into the .Json File


if sys.argv[1] == '-h' or sys.argv[1] == '-H':
	print('Format should be python .JsonToCsv ''Final.JsonFile location'' ''Adding.JsonFile location'' \n example: python ./JasonConcat.py ./FinalData.json ./Node10.json ')

else:
	mergesjson(sys.argv[1],sys.argv[2])
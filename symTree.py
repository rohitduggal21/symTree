import pprint

'''
------------------------------------------------------------
Class sysmptom is an encapsulation of a Symptom
------------------------------------------------------------

Attributes:
	(1) repr: String representation of a symptom (str)
	(2) type: Extra property of a symptom (location,severity,None)
	(3) sub: List of child symptoms

'''
class symptom:	
	def __init__(self,string,type=None):	
		self.repr = string
		self.type = type
		self.sub = []

'''
-------------------------------------------------------------
Class sysTree is an encapsulation of a Symptom Tree/Hierarchy
-------------------------------------------------------------

Attributes:
	(1) base: List of string representations of base symptoms
	(2) sym: List of object representation of symptoms (List of `symptom` objects)

Functions:	
	(1) add:
		Arguments:
			sym_list: List of `symptom` objects (list)
		Usage:	
			Create a Hierarchy of symptoms based on the input provided
	(2) getSymptomByName:	
		Arguments:
			name: Name for which `symptom` object is required (str)
		Usage:	
			Get the `symptom` object with name=name
	(3) getSiblings:	
		Arguments:	
			node_value: Node for which the siblings are required (str)
		Usage:	
			Get the sibling nodes based on the node_value provided
	(4) show:
		Usage:	
			Display the Hierarchy of symptoms

'''
class symTree:	
	def __init__(self, symptoms):	
		self.base = []
		self.sym = []
		self.add(symptoms)

	def add(self,sym_list):	
		for sym in sym_list:	
			if sym.type is None:	
				if sym.repr not in self.base:	
					self.base.append(sym.repr)
					self.sym.append(sym)
			else:	
				parent = sym.repr.split(',')[0]
				child = sym.repr.split(',')[1]
				if parent not in self.base:	
					self.base.append(parent)
					self.sym.append(sym)
				else:	
					member = self.getSymptomByName(parent)
					member.sub.append("--"+sym.type+"--"+sym.repr)

	def getSymptomByName(self,name):	
		for sym in self.sym:	
			if sym.repr==name:	
				return sym
		return None

	def getSiblings(self,node_value):	
		result = []
		if len(node_value.split(','))>1:	
			base = node_value.split(',')[0]
			sym = self.getSymptomByName(base)
			for s in sym.sub:	
				val = s.split("--")[2]
				if val != node_value:	
					result.append(val)
		else:	
			result = []
			for sym in self.sym:	
				if sym.repr != node_value:	
					result.append(sym.repr)
		return result

	def show(self):	
		for sym in self.sym:	
			print("--symptom--"+sym.repr)
			for child in sym.sub:	
				print("                             "+child)

sym = symTree([symptom("Abdominal pain"),
				   symptom("Abdominal pain,right upper quadrant","location"),
				   symptom("Abdominal pain,right lower quadrant","location"),
				   symptom("Abdominal pain,left upper quadrant","location"),
				   symptom("Abdominal pain,right upper quadrant","location"),
				   symptom("Abdominal pain,mild","severity"),
				   symptom("Abdominal pain,moderate","severity"),
				   symptom("Abdominal pain,severe","severity"),
				   symptom("Chest pain"),
				   symptom("Chest pain,left side","location"),
				   symptom("Chest pain,right side","location"),
				   symptom("Chest pain,mild","severity"),
				   symptom("Chest pain,moderate","severity"),
				   symptom("Chest pain,severe","severity")
				])


#Show Symptoms Tree
sym.show()

#Siblings 1
pprint.pprint(sym.getSiblings("Abdominal pain,right upper quadrant"))

#Siblings 2
pprint.pprint(sym.getSiblings("Abdominal pain"))

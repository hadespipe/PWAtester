class Node:
	
	def __init__(self, data=None, next=None, previous=None):
		self.data = data
		self.next = next
		self.previous = previous
	
	def __str__(self):
		return str(self.data)
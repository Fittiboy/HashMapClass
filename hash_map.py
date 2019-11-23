from datetime import datetime as t

class HashMap:
	def __init__(self, array_size):
		self.array_size = array_size
		self.array = [[None] for i in range(array_size)]

	def hash(self, key):
		sum_bytes = sum(key.encode())
		return sum_bytes % self.array_size

	def get_index(self, key):
		index = self.hash(key)
		checked_indices = []
		while self.array[index][0] and self.array[index][0] != key:
			checked_indices.append(index)
			if len(checked_indices) == self.array_size:
				return None
			index = (index + 1) % self.array_size
		return index

	def assign(self, key, value):
		index = self.get_index(key)
		if index is not None:
			self.array[index] = [key, value]
		else:
			print("Sorry, the array is full!")


	def retrieve(self, key):
		index = self.get_index(key)
		if index is not None:
			return self.array[index][1]
		else:
			print("There is no value stored for that key.")
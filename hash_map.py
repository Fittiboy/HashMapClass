class HashMap:
	def __init__(self, array_size):
		self.array_size = array_size
		self.array = [[None] for i in range(array_size)]

	def hash(self, key):
		sum_bytes = sum(key.encode())
		return sum_bytes % self.array_size

	def get_index(self, key):
		index = self.hash(key)
		jump = 1
		while self.array[index][0] and self.array[index][0] != key:
			index = (index + jump**2) % self.array_size
			jump += 1
		return index

	def assign(self, key, value):
		index = self.get_index(key)
		self.array[index] = [key, value]


	def retrieve(self, key):
		index = self.get_index(key)
		return self.array[index][1]

hash_map = HashMap(20)

for i in range(20):
	hash_map.assign(str(i), i)

print(hash_map.array)
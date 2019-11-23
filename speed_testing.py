from datetime import datetime as t
from hash_map import *

def test_speed(length):
	s = t.now()
	hash_map = HashMap(length)

	for i in range(length):
		hash_map.assign(str(i), i)

	for i in range(length):
		hash_map.retrieve(str(i))

	e = t.now()
	hm_time = e - s

	s = t.now()
	dictionary = {}
	for i in range(length):
		dictionary[str(i)] = 1

	for i in range(length):
		dictionary[str(i)]

	e = t.now()
	dict_time = e - s

	hm_string = f"{hm_time.seconds}.{hm_time.microseconds}s"
	dict_string = f"{dict_time.seconds}.{dict_time.microseconds}s"
	print(f"Creation and lookup of {length} key-value pairs took {hm_string}",
		f"for the hash table and {dict_string} for the dictionary.")

for i in range(3):
	test_speed(10 * 10 ** i)
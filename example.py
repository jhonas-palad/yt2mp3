iter_fields = iter(['a','b', 'c', 'd', 'e', 'f'])
args = [1,2,3]
for k, v in zip(iter_fields, args):
	print(k, v)


def findMaxMin(list):
	return [len(list)] if sorted(list)[0] == sorted(list)[-1] else [sorted(list)[0], sorted(list)[-1]]
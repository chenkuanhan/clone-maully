def count(input1):
	dic1 = {}
	for i in range(len(input1)):
		ddic = {input1[i]:input1.count(input1[i])}
		dic1.update(ddic)
return dic1


print(count(['a', 'b', 'c', 'a', 'c', 'a', 'x']))
import pandas as pd
def group_by_key(input2):
	df = pd.DataFrame(input2)

	data = df.groupby(['key']).sum()

	ans = data.to_dict()
return ans['value']


input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2},
{'key': 'a', 'value': 3},
{'key': 'c', 'value': 5}
]
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
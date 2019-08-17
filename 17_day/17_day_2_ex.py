import itertools

with open('17_day_input.txt') as data_doc:
	cont = list(map(int, data_doc.read().splitlines()))

results = []
for i in range(1,len(cont)): 
	for s in itertools.combinations(cont, i):
		if sum(s) == 150:
			results.append(s)

#print(min(results, key=len))

#print(len(min(results, key=len)))

z = min(map(len, results))

y = len(list(filter(lambda x: len(x) == z, results)))

print(y)
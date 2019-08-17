import time

with open('test_input.txt') as data_doc:
	data = list(map(int, data_doc.read().splitlines()))

data = range(4)

def comb(x):
	l = []
	if len(x) == 1:
		return [x]
	for c, v in enumerate(x):
		combinations = comb([j for i, j in enumerate(x) if i != c])
		for i in combinations:
			l.append([v] + i)
	return l

result = []

start = time.time()
for i in range(len(data)):
	for j in range(len(data)):
		if j == i:
			continue
		for k in range(len(data)):
			if k == i or k == j:
				continue
			result.append([data[i], data[j], data[k]])

end = time.time()
print(end-start, 's')

start = time.time()
comb(data)
end = time.time()
print(end-start, 's')
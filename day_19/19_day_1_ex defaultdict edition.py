from collections import defaultdict

with open('19_day_input.txt') as data_doc:
	initial_data = data_doc.read().splitlines()

del initial_data[-2]
word = initial_data.pop(-1)

data = defaultdict(list)
for i in initial_data:
	i = i.split(' => ')
	data[i[0]].append(i[1])

print(data)

p_m = set()

# p_m = possible molecules

for c, v in enumerate(word):
	if v in data.keys():
		for i in data[v]:
			p_m.add(word[:c] + i + word[c+1:])
	if word[c:c+2] in data.keys():
		for j in data[word[c:c+2]]:
			p_m.add(word[:c] + j + word[c+2:])

print(len(p_m))
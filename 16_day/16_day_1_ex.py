from pprint import pprint
with open('16_day_input.txt') as data_doc:
	data = list(map(str.split, data_doc.read().replace(':', '').replace(',', '').replace('Sue ', '').splitlines()))

d = {}
s = {'chi': 3, 'cat': 7, 'sam': 2, 'pom': 3, 'aki': 0,
	 'viz': 0, 'gol': 5, 'tre': 3, 'car': 2, 'per': 1}

for i in data:
	main_key = i[0]
	minor_keys = []
	values = []
	for c, v  in enumerate(i[1:]):
		if c % 2 == 0:
			minor_keys.append(v[:3])
		else:
			values.append(int(v))
	for c, v in enumerate(values):
		if v == 0:
			del values[c]
			del minor_keys[c]
	d[main_key] = dict(zip(minor_keys, values))
	d[main_key] = dict(zip(minor_keys, values))

pprint(d)

for key, val in d.items():
	if val.items() <= s.items():
		print(key, val)

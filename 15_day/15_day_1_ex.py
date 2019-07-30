from pprint import pprint
with open('15_day_input.txt') as data_doc:
	data = list(map(str.split, data_doc.read().replace(':', '').replace(',', '').splitlines()))

d = {}

for i in data:
	main_key = i[0][:2]
	minor_keys = []
	values = []
	for c, v  in enumerate(i[1:]):
		if c % 2 == 0:
			minor_keys.append(v[:3])
		else:
			values.append(int(v))
	minor_keys.append('q')
	values.append(0)
	d[main_key] = dict(zip(minor_keys, values))

pprint(d)
k = d['Sp']['cap'] * 5

print(k)
combinations = []

for a in range(0, 101):
    for b in range(0, 101):
        if a + b > 100:
            break
        for c in range(0, 101):
            if a + b + c > 100:
                break
            for d in range(0, 101):
                if a + b + c + d == 100:
                    combinations.append([a, b, c, d])
                elif a + b + c + d > 100:
                    break



def multiplication(lst):
	w = lst[0] * d['Sp']['cap'] + lst[1] * d['Bu']['cap'] + lst[2] * d['Ch']['cap'] + lst[3] * d['Ca']['cap']
	x = lst[0] * d['Sp']['dur'] + lst[1] * d['Bu']['dur'] + lst[2] * d['Ch']['dur'] + lst[3] * d['Ca']['dur']
	y = lst[0] * d['Sp']['fla'] + lst[1] * d['Bu']['fla'] + lst[2] * d['Ch']['fla'] + lst[3] * d['Ca']['fla']
	z = lst[0] * d['Sp']['tex'] + lst[1] * d['Bu']['tex'] + lst[2] * d['Ch']['tex'] + lst[3] * d['Ca']['tex']
	print(w)
	return w * x * y * z

total_score = 0
for i in combinations:
	if multiplication(i) >= total_score:
		total_score = multiplication(i)

print(total_score)

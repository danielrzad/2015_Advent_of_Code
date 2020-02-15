with open("9_day_input.txt") as data_doc:
	data = data_doc.read().replace("to", "").replace("=", "").replace("  ", " ").splitlines()


data = [s.split() for s in data]


starting_points = []
routes = []

for line in data:
	if line[0] not in starting_points:
		starting_points.append(line[0])
	if line[1] not in starting_points:
		starting_points.append(line[1])

for city in starting_points:
	sub_routes = []
	for line in data:
		if city == line[0]:
			track = []
			track.append(int(line[2]))
			track.append(city)
			track.append(line[1])
			if track not in sub_routes:
				sub_routes.append(track)
		if city == line[1]:
			track = []
			track.append(int(line[2]))
			track.append(city)
			track.append(line[0])
			if track not in sub_routes:
				sub_routes.append(track)
	for sub_route in sub_routes:
		routes.append(sub_route)

def next_city(prev):
	possible_routes = []
	for line in data:
		prev_copy = [i for i in prev]
		if prev_copy[-1] == line[0] and line[1] not in prev_copy:
			prev_copy[0] += int(line[2])
			prev_copy.append(line[1])
			if prev_copy not in possible_routes:
				possible_routes.append(prev_copy)
		if prev_copy[-1] == line[1] and line[0] not in prev_copy:
			prev_copy[0] += int(line[2])
			prev_copy.append(line[0])
			if prev_copy not in possible_routes:
				possible_routes.append(prev_copy)
	return possible_routes



while True:
	for route in routes:
		if len(route) < 9:
			for r in next_city(route):
				routes.append(r)
			routes.remove(route)
	if all([len(r) == 9 for r in routes]):
		break

distances = []
for route in routes:
	distances.append(route[0])


print(max(distances))
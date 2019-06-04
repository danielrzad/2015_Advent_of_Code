with open("3 day input.txt") as data_doc:
	data = data_doc.read()

visited_locations = [[0, 0]]

x_santa = 0
y_santa = 0

for i in range(0, len(data), 2):
	current_cords = []
	if data[i] == "^":
		y_santa += 1
	elif data[i] == "v":
		y_santa -= 1
	elif data[i] == ">":
		x_santa += 1
	elif data[i] == "<":
		x_santa -= 1
	current_cords.append(x_santa)
	current_cords.append(y_santa)
	if current_cords not in visited_locations:
		visited_locations.append(current_cords)

x_robo = 0
y_robo = 0

for i in range(1, len(data), 2):
	current_cords = []
	if data[i] == "^":
		y_robo += 1
	elif data[i] == "v":
		y_robo -= 1
	elif data[i] == ">":
		x_robo += 1
	elif data[i] == "<":
		x_robo -= 1
	current_cords.append(x_robo)
	current_cords.append(y_robo)
	if current_cords not in visited_locations:
		visited_locations.append(current_cords)

print(len(visited_locations))
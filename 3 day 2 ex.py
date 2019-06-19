with open("3 day input.txt") as data_doc:
	data = data_doc.read()

visited_locations = [[0, 0]]

x_santa = 0
y_santa = 0
x_robot = 0
y_robot = 0


for i in range(len(data)):
	if i % 2 == 0:
		current_cords_santa = []
		if data[i] == "^":
			y_santa += 1
		elif data[i] == "v":
			y_santa -= 1
		elif data[i] == ">":
			x_santa += 1
		elif data[i] == "<":
			x_santa -= 1
		current_cords_santa.append(x_santa)
		current_cords_santa.append(y_santa)
		if current_cords_santa not in visited_locations:
			visited_locations.append(current_cords_santa)
	else:
		current_cords_robot = []
		if data[i] == "^":
			y_robot += 1
		elif data[i] == "v":
			y_robot -= 1
		elif data[i] == ">":
			x_robot += 1
		elif data[i] == "<":
			x_robot -= 1
		current_cords_robot.append(x_robot)
		current_cords_robot.append(y_robot)
		if current_cords_robot not in visited_locations:
			visited_locations.append(current_cords_robot)

print(len(visited_locations))
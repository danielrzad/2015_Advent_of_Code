with open("3 day input.txt") as data_doc:
	data = data_doc.read()

visited_locations = [[0,0]]
x = 0
y = 0

for s in data:
	current_cords = []
	if s == "^":
		y += 1
	elif s == "v":
		y -= 1
	elif s == ">":
		x += 1
	elif s == "<":
		x -= 1
	current_cords.append(x)
	current_cords.append(y)
	if current_cords not in visited_locations:
		visited_locations.append(current_cords)

print(len(visited_locations))

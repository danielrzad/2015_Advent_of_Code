with open("6_day_input.txt") as data_doc:
	data = data_doc.read().replace("turn ", "").splitlines()

grid = [[0] * 1000 for i in range(1000)]

def off(startX, startY, stopX, stopY):
	for y in range(startY, stopY + 1):
		for x in range(startX, stopX + 1):
			if grid[y][x] > 0:
				grid[y][x] -= 1

def on(startX, startY, stopX, stopY):
	for y in range(startY, stopY + 1):
		for x in range(startX, stopX + 1):
			grid[y][x] += 1

def toggle(startX, startY, stopX, stopY):
	for y in range(startY, stopY + 1):
		for x in range(startX, stopX + 1):
			grid[y][x] += 2

for i in range(len(data)):
	data[i] = data[i].replace(",", " ").split()
	data[i][1] = int(data[i][1])
	data[i][2] = int(data[i][2])
	data[i][4] = int(data[i][4])
	data[i][5] = int(data[i][5])
	if data[i][0] == "off":
		off(data[i][1], data[i][2], data[i][4], data[i][5])
	if data[i][0] == "on":
		on(data[i][1], data[i][2], data[i][4], data[i][5])
	if data[i][0] == "toggle":
		toggle(data[i][1], data[i][2], data[i][4], data[i][5])

total_brightness = 0

for row in grid:
	for light in row:
		total_brightness += light

print(total_brightness)
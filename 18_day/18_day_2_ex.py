with open('18_day_input.txt') as data_doc:
	data = data_doc.read().splitlines()

def check_on_neighbors(x, y, grid, z):
	on_cont = -1
	off_cont = 0
	os_x_1, os_x_2 = x-1, x+2
	os_y_1, os_y_2 = y-1, y+2
	if x in [0, -1] or y in [0, -1]:
		if x == 0:
			os_x_1 = 0
		elif grid[x] == grid[-1]:
			os_x_1 = -2
			os_x_2 = None
		if y == 0:
			os_y_1 = 0
		elif grid[y] == grid[-1]:
			os_y_1 = -2
			os_y_2 = None		
	for i in grid[os_x_1:os_x_2]:
		for j in i[os_y_1:os_y_2]:
			if j == z:
				on_cont += 1
			else:
				off_cont += 1
	if on_cont in [2, 3]:
		return True
	else:
		return False

def check_off_neighbors(x, y, grid, z):
	on_cont = 0
	off_cont = -1
	os_x_1, os_x_2 = x-1, x+2
	os_y_1, os_y_2 = y-1, y+2
	if x in [0, -1] or y in [0, -1]:
		if x == 0:
			os_x_1 = 0
		elif grid[x] == grid[-1]:
			os_x_1 = -2
			os_x_2 = None
		if y == 0:
			os_y_1 = 0
		elif grid[y] == grid[-1]:
			os_y_1 = -2
			os_y_2 = None		
	for i in grid[os_x_1:os_x_2]:
		for j in i[os_y_1:os_y_2]:
			if j == z:
				off_cont += 1
			else:
				on_cont += 1
	if on_cont == 3:
		return True
	else:
		return False

# print(data[0])
data[0] = '#' + data[0][1:-1] + '#'
# print(data[0])
data[-1] = '#' + data[-1][1:-1] + '#'

def first_last_row():
	#zrobic iterator do 1 i ostatniego rzedu 
	for co, va in enumerate(v):
			if va == '#':
				if check_on_neighbors(c, co, data, va):
					new_row.append('#')
				else:
					new_row.append('.')
			if va == '.':
				if check_off_neighbors(c, co, data, va):
					new_row.append('#')
				else:
					new_row.append('.')

for r in data:
	print(r)

print()

for i in range(4):
	new_data = []
	for c, v in enumerate(data):
		print(data[c])
		new_row = []
		for co, va in enumerate(v):
			if va == '#':
				if check_on_neighbors(c, co, data, va):
					new_row.append('#')
				else:
					new_row.append('.')
			if va == '.':
				if check_off_neighbors(c, co, data, va):
					new_row.append('#')
				else:
					new_row.append('.')
		new_data.append(new_row)
	data = new_data
	for r in data:
		print(r)
	print()

lights_on = 0

for r in data:
	for c in r:
		for i in c:
			if i == '#':
				lights_on += 1

print(lights_on)
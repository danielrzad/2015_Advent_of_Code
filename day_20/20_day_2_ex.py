with open('18_day_input.txt') as data_doc:
	data = data_doc.read().splitlines()

data[0] = '#' + data[0][1:-1] + '#'
data[-1] = '#' + data[-1][1:-1] + '#'

# r_idx, y, (function) = index of acctual row
# row, r(function)  = acctual row (value)
# c_idx, x(function) = index of acctual column
# val,v(function)  = acctual item (value)

def check_neighbors(y, x, r, grid, val):
	on_cont = 0
	os_y_1, os_y_2 = y-1, y+2
	os_x_1, os_x_2 = x-1, x+2
	if y == 0 and x == 0:
		return '#'
	elif y == 0 and x == len(r) - 1:
		return '#'
	elif y == len(grid) - 1 and x == len(r) - 1:
		return '#'
	elif y == len(grid) - 1 and x == 0:
		return '#'
	elif y == 0:
		os_y_1 = 0
	elif y == len(grid) - 1:
		os_y_2 = None
	elif x == 0:
		os_x_1 = 0
	elif x == len(r) - 1:
		os_x_2 = None
	for i in grid[os_y_1:os_y_2]:
		for j in i[os_x_1:os_x_2]:
			if j == '#':
				on_cont += 1	
	if val == '#' and on_cont in [3, 4]:
		return '#'
	if val == '.' and on_cont == 3:
		return '#'
	else:
		return '.'

for i in range(100):
	new_data = []
	for r_idx, row in enumerate(data):
		new_row = []
		for c_idx, val in enumerate(row):
			new_row.append(check_neighbors(r_idx, c_idx, row, data, val))
		new_data.append(new_row)
	data = new_data

lights_on = 0

for r in data:
	for c in r:
		for i in c:
			if i == '#':
				lights_on += 1

print(lights_on)
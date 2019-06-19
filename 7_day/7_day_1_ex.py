with open("7_day_input.txt") as data_doc:
	data = data_doc.read().splitlines()

signals = {}

for i in range(len(data)):
	data[i] = data[i].split()
	for j in range(len(data[i])):
		try:
			data[i][j] = int(data[i][j])
		except ValueError:
			continue

def and_operation(input1, input2, output):
	signal = input1 & input2
	signals[output] = signal

def or_operation(input1, input2, output):
	signal = input1 | input2
	signals[output] = signal

def l_shift_operation(input1, input2, output):
	signal = input1 << input2
	signals[output] = signal

def r_shift_operation(input1, input2, output):
	signal = input1 >> input2
	signals[output] = signal

def not_operation(input1, output):
	num_bin = bin(input1)[2:].zfill(16)
	num_bin_comp = ""
	for i in range(len(num_bin)):
		if num_bin[i] == "0":
			num_bin_comp += "1"
		else:
			num_bin_comp += "0"
	signals[output] = int(num_bin_comp, 2)



while True:
	for i in range(len(data)):
		try:
			if len(data[i]) == 3:
				try:
					if isinstance(data[i][0], int) == True:
						signals[data[i][2]] = data[i][0]
						del data[i]
					elif isinstance(data[i][0], str) == True:
						signals[data[i][2]] = signals[data[i][0]]
						del data[i]
				except KeyError:
					continue
		except IndexError:
			continue
		if isinstance(data[i][0], int) == True and len(data[i]) == 3:
			signals[data[i][2]] = data[i][0]
		try:
			if data[i][0] in signals.keys() and data[i][2] in signals.keys():
				if data[i][1] == "AND":
					and_operation(signals[data[i][0]], signals[data[i][2]], data[i][4])
				if data[i][1] == "OR":
					or_operation(signals[data[i][0]], signals[data[i][2]], data[i][4])
				if data[i][1] == "LSHIFT":
					l_shift_operation(signals[data[i][0]], signals[data[i][2]], data[i][4])
				if data[i][1] == "RSHIFT":
					r_shift_operation(signals[data[i][0]], signals[data[i][2]], data[i][4])
				del data[i]
			elif data[i][0] in signals.keys() and isinstance(data[i][2], int) == True:
				if data[i][1] == "AND":
					and_operation(signals[data[i][0]], data[i][2], data[i][4])
				if data[i][1] == "OR":
					or_operation(signals[data[i][0]], data[i][2], data[i][4])
				if data[i][1] == "LSHIFT":
					l_shift_operation(signals[data[i][0]], data[i][2], data[i][4])
				if data[i][1] == "RSHIFT":
					r_shift_operation(signals[data[i][0]], data[i][2], data[i][4])
				del data[i]
			elif data[i][2] in signals.keys() and isinstance(data[i][0], int) == True:
				if data[i][1] == "AND":
					and_operation(data[i][0], signals[data[i][2]], data[i][4])
				if data[i][1] == "OR":
					or_operation(data[i][0], signals[data[i][2]], data[i][4])
				if data[i][1] == "LSHIFT":
					l_shift_operation(data[i][0], signals[data[i][2]], data[i][4])
				if data[i][1] == "RSHIFT":
					r_shift_operation(data[i][0], signals[data[i][2]], data[i][4])
				del data[i]
			elif data[i][0] == "NOT":
				if data[i][1] in signals.keys():
					not_operation(signals[data[i][1]], data[i][3])
					del data[i]
				if isinstance(data[i][1], int) == True:
					not_operation(data[i][1], data[i][3])
					del data[i]
		except IndexError:
			continue
	if "a" in signals.keys():
		print(signals["a"])
		break

with open("8_day_input.txt") as data_doc:
	data = data_doc.read().splitlines()

code_lenght = 0
string_lenght = 0

for i in range(len(data)):
	code_lenght += len(data[i])
	k = len(data[i])
	j = 0
	line_lenght = 0
	while j != k:
		if data[i][j:j+2] == '\\x':
			string_lenght -= 3
			j += 1
		elif data[i][j:j+2] == '\\\\':
			string_lenght -= 1
			j += 1
		elif data[i][j:j+2] == '\\"':
			string_lenght -= 1
			j += 1
		if k == j - 1:
			break
		else:
			j += 1
	string_lenght += len(data[i][1:-1])

print(code_lenght - string_lenght)
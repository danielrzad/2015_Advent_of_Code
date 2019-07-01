with open("8_day_input.txt") as data_doc:
	data = data_doc.read().splitlines()

code_lenght = 0
string_lenght = 0

for i in range(len(data)):
	code_lenght += len(data[i])
	for j in range(len(data[i])):
		if data[i][j:j+2] == '\\\\':
			data[i] = data[i][:j] + data[i][j+1:]
		if data[i][j:j+2] == '\\"':
			data[i] = data[i][:j] + data[i][j+1:]
		if data[i][j:j+2] == '\\x':
			try:
				if bytearray.fromhex(data[i][j+2:j+4]).decode().isprintable() == True:
					data[i] = data[i][:j] + bytearray.fromhex(data[i][j+2:j+4]).decode() + data[i][j+4:]
			except (UnicodeDecodeError, ValueError):
				continue
	string_lenght += len(data[i][1:-1])

print(code_lenght)
print(string_lenght)
print(code_lenght - string_lenght)
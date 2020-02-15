with open("8_day_input.txt") as data_doc:
	data = data_doc.read().splitlines()

code_lenght = 0
encoded_lenght = 0

for i in data:
	code_lenght += len(i)
	for j in i:
		if j == '"':
			encoded_lenght += 2
		elif j == '\\':
			encoded_lenght += 2
		else:
			encoded_lenght += 1
	encoded_lenght += 2

print(encoded_lenght - code_lenght)
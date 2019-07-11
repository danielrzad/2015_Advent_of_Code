with open("10_day_input.txt") as data_doc:
	data = data_doc.read()

result = ""
duplicate_num = 1
for i in range(40):
	for i in range(len(data)):
		try:
			if data[i] == data[i+1]:
				duplicate_num += 1
			elif data[i] == data[i-1] and data[i] != data[i+1]:
				result += str(duplicate_num)
				result += data[i]
				duplicate_num = 1
			elif data[i] != data[i-1] and data[i] != data[i+1]:
				result += str(duplicate_num)
				result += data[i]
		except IndexError:
				result += str(duplicate_num)
				result += data[i]
	data = result
	result = ""

print(len(data))
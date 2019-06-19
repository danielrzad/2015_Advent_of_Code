with open("8_day_input.txt") as data_doc:
	data = data_doc.read().splitlines()

data = ['""', '"abc"', '"aaa\"aaa"', '"\x27"']

for i in range(len(data)):
	print(len(data[i]))
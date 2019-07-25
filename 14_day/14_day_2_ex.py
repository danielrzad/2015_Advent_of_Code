with open("14_day_input.txt") as data_doc:
	initial_data = map(str.split, data_doc.read().splitlines())

data = []
race_lenght = 2503

for lst in initial_data:
	data.extend([[lst[0], int(lst[3]), int(lst[6]), int(lst[13])]])
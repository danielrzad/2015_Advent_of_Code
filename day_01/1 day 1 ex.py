with open("1 day input.txt") as data_doc:
	data = data_doc.read()

current_floor = 0

for s in data:
	if s == "(":
		current_floor += 1
	else:
		current_floor -= 1

print(current_floor)
with open("1 day input.txt") as data_doc:
	data = data_doc.read()

current_floor = 0

for i in range(len(data)):
	if current_floor < 0:
		print(i)
		break
	elif data[i] == ("("):
		current_floor += 1
	else:
		current_floor -= 1

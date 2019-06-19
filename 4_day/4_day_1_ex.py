import hashlib 

with open("4_day_input.txt") as data_doc:
	start_data = data_doc.read()

data = ""
number = 0
while True:
	data = start_data + str(number)
	if hashlib.md5(data.encode("utf-8")).hexdigest()[:5] == "00000":
		print(number)
		break
	else:
		number += 1
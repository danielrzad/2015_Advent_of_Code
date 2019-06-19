import hashlib 

with open("4 day input.txt") as data_doc:
	start_data = data_doc.read()

data = ""
number = 0
while True:
	data = start_data + str(number)
	if hashlib.md5(data.encode("utf-8")).hexdigest()[:6] == "000000":
		print(number)
		break
	else:
		number += 1
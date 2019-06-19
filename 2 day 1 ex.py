with open("2 day input.txt") as data_doc:
	data = data_doc.read().splitlines()

# d = dimensions
d = {"l": [], "w": [], "h": []}

for i in range(len(data)):
	data[i] = data[i].split("x")
	d["l"].append(int(data[i][0]))
	d["w"].append(int(data[i][1]))
	d["h"].append(int(data[i][2]))

paper_needed = 0

for i in range(len(d["l"])):
	sides = []
	sides.append(d["l"][i] * d["w"][i])
	sides.append(d["w"][i] * d["h"][i])
	sides.append(d["h"][i] * d["l"][i])
	for j in sides:
		paper_needed += j * 2
	paper_needed += min(sides)

print(paper_needed)
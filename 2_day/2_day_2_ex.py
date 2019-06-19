with open("2_day_input.txt") as data_doc:
	data = [s.split("x") for s in data_doc.read().splitlines()]

paper_needed = 0

for i in range(len(data)):
	for j in range(len(data[i])):
		data[i][j] = int(data[i][j])
	paper_needed += data[i][0] * data[i][1] * data[i][2]
	data[i].remove(max(data[i]))
	paper_needed += 2 * data[i][0] + 2* data[i][1]


print(paper_needed)


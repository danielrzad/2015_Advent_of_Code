with open("13_day_input.txt") as data_doc:
	data = [s.replace(".", "") .split()for s in data_doc.read().splitlines()]

relations = []
persons = set()

for line in data:
	persons.add(line[0])
	persons.add(line[-1])
	persons_lst = []
	if line[2] == "gain":
		persons_lst.append(int(line[3]))
	elif line[2] == "lose":
		persons_lst.append(-int(line[3]))
	persons_lst.append(line[0])
	persons_lst.append(line[10])
	relations.append(persons_lst)

connections = relations[:]


def find_next(lst):
	relationships = []
	for relation in relations:
		if lst[-1] == relation[1] and relation[2] not in lst:
			temp_lst = lst[:]
			temp_lst[0] += relation[0]
			temp_lst.append(relation[2])
			if temp_lst not in relationships:
				relationships.append(temp_lst)
	return relationships

final_lst = []

while all([len(i) == (len(persons) + 1) for i in connections]) != True:
	for connection in connections:
		if len(connection) < 9:
			connections.extend(find_next(connection))
			connections.remove(connection)
		if len(connection) == 9:
			#dorobic liczenie od tylu
			for count, item in reversed(list(enumerate(connection))):
			for rel in relations:
				#do znajdywania powiazan pomiedzy ostatnim a pierwszym i pierwszym a ostatnim
				if connection[1] == rel[2] and connection[-1] == rel[1]:
					connection[0] += rel[0]
				if connection[1] == rel[1] and connection[-1] == rel[2]:
					connection[0] += rel[0]
			final_lst.append(connection)
			connections.remove(connection)
			break

highest_happines = final_lst[0][0]
print(final_lst)
for lst in final_lst:
	if lst[0] > highest_happines:
		highest_happines = lst[0]




for count, item in reversed(enumerate(final_lst)):
	print("chuj")

with open("5 day input.txt") as data_doc:
	data = data_doc.read().splitlines()


def first_condition_check(string):
	first_req = 0
	second_req = 0
	for i in range(len(string) - 2):
		if string[i:i+2] in string[i+2:]:
			first_req += 1
		if string[i] != string[i+2]:
			second_req += 1
		if first_req > 0 and second_req > 0:
			return True

def second_condition_check(string):
	counter = 0
	for i in range(len(string) - 2):
		if string[i] == string[i+2]:
			counter += 1
	if counter > 0:
		return True

nice_string_counter = 0

for line in data:
	if first_condition_check(line) and second_condition_check(line):
		nice_string_counter += 1

print(nice_string_counter)
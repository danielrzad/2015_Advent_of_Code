with open("5 day input.txt") as data_doc:
	data = data_doc.read().splitlines()


def first_condition_check(string):
	for i in range(len(string) - 2):
		if string[i:i+2] in string[i+2:]:
			return True

def second_condition_check(string):
	for i in range(len(string) - 2):
		if string[i] == string[i+2]:
			return True

nice_string_counter = 0

for line in data:
	if first_condition_check(line) and second_condition_check(line):
		nice_string_counter += 1

print(nice_string_counter)

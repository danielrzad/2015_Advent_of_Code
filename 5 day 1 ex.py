with open("5 day input.txt") as data_doc:
	data = data_doc.read().splitlines()

def first_condition_check(string):
	counter = 0
	vowels = "aeiou"
	for s in line:
		if s in vowels:
			counter += 1
	if counter >= 3:
		return True

def second_condition_check(string):
	counter = 0
	for i in range(len(string) - 1):
		if string[i] == string[i+1]:
			counter += 1
	if counter >= 1:
		return True

def third_condition_check(string):
	counter = 0
	bad_strings = ["ab", "cd", "pq", "xy"]
	for s in bad_strings:
		if s in string:
			counter += 1
	if counter == 0:
		return True

nice_strings_counter = 0

for line in data:
	conditions_check = 0
	if first_condition_check(line):
		conditions_check += 1
	if second_condition_check(line):
		conditions_check += 1
	if third_condition_check(line):
		conditions_check += 1
	if conditions_check == 3:
		nice_strings_counter += 1

print(nice_strings_counter)
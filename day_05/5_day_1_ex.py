with open("5_day_input.txt") as data_doc:
	data = data_doc.read().splitlines()

def first_condition_check(string):
	counter = 0
	vowels = set("aeiou")
	for s in line:
		if s in vowels:
			counter += 1
	if counter >= 3:
		return True

def second_condition_check(string):
	for i in range(len(string) - 1):
		if string[i] == string[i+1]:
			return True

def third_condition_check(string):
	counter = 0
	bad_strings = ["ab", "cd", "pq", "xy"]
	for s in bad_strings:
		if s in string:
			return False
	return True

nice_strings_counter = 0

for line in data:
	if first_condition_check(line) and second_condition_check(line) and third_condition_check(line):
		nice_strings_counter += 1

print(nice_strings_counter)
with open("11_day_input.txt") as data_doc:
	data = data_doc.read()

alphabet = "abcdefghijklmnopqrstuvwxyz"
forbbiden_letters = "iol"

def first_con(password):
	for i in range(len(alphabet) - 2):
		if alphabet[i:i+3] in password:
			return True

def second_con(password):
	if any(s in password for s in forbbiden_letters):
		return False
	return True

def third_con(password):
	pairs = []
	for i in range(len(password) - 1):
		if password[i] == password[i+1] and password[i:i+2] not in pairs:
			pairs.append(password[i:i+2])
	if len(pairs) >= 2:
		return True

def letter_increasement(password):
	password = list(password)
	for i, l in reversed(list(enumerate(password))):
		try:
			next_letter = alphabet[alphabet.find(l) + 1]
			password[i] = next_letter
			return "".join(password)
		except IndexError:
			password[i] = alphabet[0]
			continue

good_pass_counter = 0
while True:
	if first_con(data) and second_con(data) and third_con(data):
		good_pass_counter += 1
		if good_pass_counter == 2:
			print(data)
			break
	data = letter_increasement(data)
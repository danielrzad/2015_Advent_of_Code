alphabet = "abcdefghijklmnopqrstuvwxyz"

data = "cqjxxyyy"

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

for i in range(50):
	print(data)
	data = letter_increasement(data)
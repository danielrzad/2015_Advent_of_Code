with open('20_day_input.txt') as data_doc:
	data = int(data_doc.read())

print(data)


elfs = []

def elf_generator(n):
	elf = []
	elf.append(n)
	elf.append(n * 10)
	return elf


# for i in range(1, 11):
# 	elfs.append(elf_generator(i))
# 	presents = 0
# 	for j in elfs:
# 		if i % j[0] == 0:
# 			presents += j[1]
# 	print(i)
# 	print(presents)
# 	print()


# print(elfs)

i = 1
while True:
	elfs.append(elf_generator(i))
	presents = 0
	for j in elfs:
		if i % j[0] == 0:
			presents += j[1]
	print(presents)
	if presents >= data:
		print(i)
		break
	else:
		i += 1



"""
g = 150
good_combs = 0
#print('cont', cont)

comb = [[i] for i in cont]
#print('comb', comb)


def find_next(lst):
	new_lst = []
	for i in cont:
		temp_lst = lst[:]
		if i not in lst:
			temp_lst.append(i)
			#print('temp_lst', temp_lst)
			new_lst.append(temp_lst)
	#print('new_lst', new_lst)
	return new_lst

for c, v in enumerate(comb):
	print(good_combs)
	if sum(v) == g:
		good_combs += 1
		comb.remove(v)
	if sum(v) > 150:
		comb.remove(v)
	else:
		if find_next(v) not in comb:
			comb.extend(find_next(v))
			comb.remove(v)
	#print('new_comb', comb)

print(good_combs)
"""
import itertools

with open('17_day_input.txt') as data_doc:
	cont = list(map(int, data_doc.read().splitlines()))


numbers = cont
result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == 150]
print(result)
print(len(result))
with open("14_day_input.txt") as data_doc:
	initial_data = map(str.split, data_doc.read().splitlines())

data = []
race_lenght = 2503

for lst in initial_data:
	data.extend([[lst[0], int(lst[3]), int(lst[6]), int(lst[13])]])

def speedometer(speed, speed_time, rest_time, race_duration):
	distance = 0
	full_cycles = race_duration // (speed_time + rest_time)
	race_duration -= full_cycles * (speed_time + rest_time)
	distance += speed * speed_time * full_cycles
	working_lst = [1] * speed_time
	for i in working_lst:
		if race_duration >= 1:
			distance += speed
			race_duration -= 1
	return distance

dist = 0
for l in data:
	if speedometer(l[1], l[2], l[3], race_lenght) >= dist:
		dist = speedometer(l[1], l[2], l[3], race_lenght)

print(dist)
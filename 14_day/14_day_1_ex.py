with open("14_day_input.txt") as data_doc:
	initial_data = map(str.split, data_doc.read().splitlines())

data = []
race_lenght = 2503

for lst in initial_data:
	data.extend([[lst[0], int(lst[3]), int(lst[6]), int(lst[13])]])
print(data)
def speedometer(speed, speed_time, rest_time, race_duration):
	distance = 0
	full_cycles = race_duration // (speed_time + rest_time)
	race_duration -= full_cycles * (speed_time + rest_time)
	distance += speed * speed_time * full_cycles
	for i in range(speed_time):
		if race_duration >= 1:
			distance += speed
			race_duration -= 1
	return distance

print(max(map(lambda x: speedometer(*x[1:4], race_lenght), data)))

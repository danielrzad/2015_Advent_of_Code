with open("14_day_input.txt") as data_doc:
	initial_data = map(str.split, data_doc.read().splitlines())

race_lenght = 2503
reindeers = {}

for lst in initial_data:
	reindeers[lst[0]] = {'speed': int(lst[3]), 'speed_time': int(lst[6]),
						 'speed_time_left': int(lst[6]), 'rest_time': int(lst[13]), 
						 'actual_rest_time': int(lst[13]), 'distance': 0,
						 'points': 0}

def distance_per_sec(reindeeer_dic):
	if reindeeer_dic['speed_time_left'] >= 1:
		reindeeer_dic['speed_time_left'] -= 1
		reindeeer_dic['distance'] += reindeeer_dic['speed']
	elif reindeeer_dic['speed_time_left'] == 0:
		reindeeer_dic['actual_rest_time'] -= 1
		if reindeeer_dic['actual_rest_time'] == 0:
			reindeeer_dic['actual_rest_time'] = reindeeer_dic['rest_time']
			reindeeer_dic['speed_time_left'] = reindeeer_dic['speed_time'] 

def points_per_sec():
	sec_winner = [0, 'place_holder']
	for key in reindeers.keys():
		if reindeers[key]['distance'] > sec_winner[0]:
			sec_winner = [reindeers[key]['distance'], key]
		elif reindeers[key]['distance'] == sec_winner[0]:
			sec_winner.append(key)
	for k in sec_winner[1:]:
		reindeers[k]['points'] += 1

for i in range(race_lenght):
	for key in reindeers.keys():
		distance_per_sec(reindeers[key])
	points_per_sec()

max_pointes = 0

for key in reindeers.keys():
	if reindeers[key]['points'] >= max_pointes:
		max_pointes = reindeers[key]['points']

print(max_pointes)
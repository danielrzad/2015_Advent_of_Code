import json
from pprint import pprint

with open("12_day_input.JSON", "r") as data_doc:
	data = json.load(data_doc)


#print(type(data))
#pprint(data)

#for key, value in data.items():
#	print(type(key), type(value))


num_sum = 0

def get_dic_val(dic):
	global num_sum
	for val in dic.values():
		if type(val) == int:
			num_sum += val
		if type(val) == list:
			get_lst_val(val)
		if type(val) == dict:
			get_dic_val(val)


def get_lst_val(lst):
	global num_sum
	for val in lst:
		if type(val) == int:
			num_sum += val
		if type(val) == list:
			get_lst_val(val)
		if type(val) == dict:
			get_dic_val(val)



for val in data.values():
	if type(val) == str:
		continue
	if type(val) == list:
		get_lst_val(val)
	else:
		get_dic_val(val)

print(num_sum)
for key, val in d.items():
	cond = 0
	for k, v in val.items():
		if k not in ['cat', 'tre', 'pom', 'gol']:
			if v == s[k]:
				cond += 1
		elif k in ['cat', 'tre', 'pom', 'gol']:	
			if k == 'cat' or k == 'tre':
				if v > s[k]:
					cond += 1
			elif k == 'pom' or k == 'gol':
				if v < s[k]:
					cond += 1
	if cond == 3:
		print(key)
		break
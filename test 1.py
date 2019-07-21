relations = [[368, 'Eric', 'Carol', 'Frank', 'George', 'David', 'Alice', 'Bob', 'Mallory'], 
			[143, 'Eric', 'Frank', 'Bob', 'Alice', 'George', 'Mallory', 'Carol', 'David'],
			 [50, 'Eric', 'Frank', 'Bob', 'Mallory', 'Alice', 'David', 'Carol', 'George'], 
			 [18, 'Eric', 'Frank', 'Mallory', 'Bob', 'David', 'Alice', 'Carol', 'George'],]

connecitons = [[368, 'Eric', 'Carol', 'Frank', 'George', 'David', 'Alice', 'Bob', 'Mallory'], 
			[143, 'Eric', 'Frank', 'Bob', 'Alice', 'George', 'Mallory', 'Carol', 'David'],
			 [50, 'Eric', 'Frank', 'Bob', 'Mallory', 'Alice', 'David', 'Carol', 'George'], 
			 [18, 'Eric', 'Frank', 'Mallory', 'Bob', 'David', 'Alice', 'Carol', 'George'],]

for count, item in reversed(list(enumerate(connecitons[0][2:], 2))):
	print(count, item)


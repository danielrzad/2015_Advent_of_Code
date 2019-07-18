relations = [[368, 'Eric', 'Carol', 'Frank', 'George', 'David', 'Alice', 'Bob', 'Mallory'], 
			[143, 'Eric', 'Frank', 'Bob', 'Alice', 'George', 'Mallory', 'Carol', 'David'],
			 [50, 'Eric', 'Frank', 'Bob', 'Mallory', 'Alice', 'David', 'Carol', 'George'], 
			 [18, 'Eric', 'Frank', 'Mallory', 'Bob', 'David', 'Alice', 'Carol', 'George'],]

connecitons = [[368, 'Eric', 'Carol', 'Frank', 'George', 'David', 'Alice', 'Bob', 'Mallory'], 
			[143, 'Eric', 'Frank', 'Bob', 'Alice', 'George', 'Mallory', 'Carol', 'David'],
			 [50, 'Eric', 'Frank', 'Bob', 'Mallory', 'Alice', 'David', 'Carol', 'George'], 
			 [18, 'Eric', 'Frank', 'Mallory', 'Bob', 'David', 'Alice', 'Carol', 'George'],]

persons = {'George', 'David', 'Mallory', 'Alice', 'Frank', 'Eric', 'Bob', 'Carol'}

print(all([len(i) == 9 for i in relations]))

relations.extend(connecitons)

print(relations)

"""
while all([len(i) for i in relations]) != 9:
	print("true")
"""
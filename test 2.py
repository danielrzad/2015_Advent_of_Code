with open('test_input.txt') as data_doc:
	data = data_doc.read().replace(' - zaproszenie.docx', '').replace('.docx', '').replace(' zaproszenie', '').splitlines()


data = set(data)
print(data)

print('\n'.join(data))
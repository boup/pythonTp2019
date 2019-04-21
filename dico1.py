import csv

def read_dict(file_location):
	with open(file_location, 'r+') as csv_file:
		reader = csv.DictReader(csv_file)
		print(str([row for row in reader]))
		return [row for row in reader]
def write_dict(file_location, dictionaries):
	with open(file_location, 'w+') as csv_file:
		headers = [k for k in dictionaries[0]]
		writer = csv.DictWriter(csv_file, fieldnames=headers)
		writer.writeheader()
		for dictionary in dictionaries:
			writer.writerow(dictionary)

def dict_test():
	input_rows = []
	keep_going = True
	while keep_going:
		name = input("Name: ")
		last_name = input("Last Name: ")
		age = input("Age: ")
		input_rows.append({"name": name, "last_name": last_name, "age": age})
		ui_keep_going = input("continue? (y/N): ")
		if ui_keep_going != "y":
			keep_going = False

	print(str(input_rows))
	write_dict('dict.csv', input_rows)
	written_value = read_dict('dict.csv')
	print(str(written_value))

dict_test()

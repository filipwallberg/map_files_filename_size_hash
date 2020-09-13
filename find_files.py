import os
import hashlib

# Remember to set path.
# The .csv file will be placed next to this file.

path = "/Users/filip/Desktop/logoer"
files_list_save = []

for root, dirs, files in os.walk(path):
	for name in files:

		file_to_list_name = root + os.sep + name
		file_to_list_hash = hashlib.md5(open(file_to_list_name,'rb').read()).hexdigest()
		file_to_list_size = os.stat(file_to_list_name).st_size / 1000000

		if(os.stat(file_to_list_name).st_size > 0.01):

			print("File name with path:\n" + file_to_list_name)
			print("File size:\n" + str(file_to_list_size) + " mb")
			print("File hash:\n" + file_to_list_hash)
			print("---***---***---***---***---***---***")

			file_save_to_list = [name, file_to_list_name, file_to_list_size, file_to_list_hash]
			files_list_save.append(file_save_to_list)

		file_to_list_hash = ""
		file_to_list_size = ""
		file_to_list_name = ""

csv_file = open("files_with_hash.csv","w")
csv_file.write("file;file with path;size;hash\n")

for file in files_list_save:
	csv_file.write(file[0] + ";" + file[1] + ";" + str(file[2]) + ";" + file[3] + "\n")

csv_file.close()

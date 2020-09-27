import os
import time
import hashlib

# Script by Filip Wallberg, wallberg@gmail.com, twitter.com/fiwa
# License: Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
# https://creativecommons.org/licenses/by-nc-sa/4.0/

# Remember to set path @ line 12.
# The .csv file ('files_with_hash.csv') will be placed next to this file.

path = "../logoer"
files_list_save = []

for root, dirs, files in os.walk(path):
	for name in files:

		attempts_to_check_file = 1
		file_to_list_name = "-"
		file_to_list_hash = "-"
		file_to_list_size = 0
		file_to_list_date = "-"
		file_to_list_status = "-"

		file_to_list_name = root + os.sep + name

		while attempts_to_check_file < 4:

			try:
				file_to_list_hash = hashlib.md5(open(file_to_list_name,'rb').read()).hexdigest()
				file_to_list_size = os.stat(file_to_list_name).st_size / 1000000
				file_to_list_date = time.ctime(os.path.getmtime(file_to_list_name))
				file_to_list_status = "checked"
				break
			except:
				attempts_to_check_file += 1
				file_to_list_status = "error"
				pass

		print("File: " + file_to_list_name)
		print("Status: " + file_to_list_status)
		print("---***---***---***---***---***---***")

		file_save_to_list = [name, file_to_list_name, file_to_list_size, file_to_list_hash, file_to_list_date, file_to_list_status]
		files_list_save.append(file_save_to_list)

csv_file = open("files_with_hash.csv","w")
csv_file.write("file;;;file with path;;;size;;;hash;;;date;;;status\n")

for file in files_list_save:
	csv_file.write(file[0] + ";;;" + file[1] + ";;;" + str(file[2]) + ";;;" + file[3] + ";;;" + file[4] + ";;;" + file[5] + "\n")

csv_file.close()
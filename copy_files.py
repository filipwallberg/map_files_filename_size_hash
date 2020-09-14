import os
import shutil

# Script by Filip Wallberg, wallberg@gmail.com, twitter.com/fiwa
# License: Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
# https://creativecommons.org/licenses/by-nc-sa/4.0/

# Remember to set search for and replace with @ line 11 + 12
# The .csv file ('files_to_copy.csv') must be placed next to this file. The file can only contain one column with the path and name of file.

replace_search_for = ""
replace_replace_with = ""

csv_file = open("files_to_copy.csv","r")
csv_file_lines = csv_file.readlines() 

for line in csv_file_lines:
	attempts_to_copy_file = 0

	while attempts_to_copy_file < 4:
		try:
			line = line.replace('"', '')
			line = line.strip()
			original_file = line
			new_file = line.replace(replace_search_for, replace_replace_with)
			os.makedirs(os.path.dirname(new_file), exist_ok=True)
			shutil.copy2(original_file, new_file)
			break
		except:
			attempts_to_copy_file += 1
			if(attempts_to_copy_file == 3):
				print('Error copying ' + line)
			pass
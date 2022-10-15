#Question 13: Given a file create its zip archive.

from zipfile import ZipFile
zip_file = ZipFile('temp.zip','w')
zip_file.write('readme1.txt')
zip_file.write('re.txt')
zip_file.close()


#Question 14: Delete a file.

import os
os.remove("temp.zip")


#Question 15: Print all the files in a given directory.
 
# Get the list of all files and directories
path = "D:\yogita_course"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)

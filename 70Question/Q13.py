#Question 13: Given a file create its zip archive.

from zipfile import ZipFile
zip_file = ZipFile('temp.zip','w')
zip_file.write('readme1.txt')
zip_file.write('re.txt')
zip_file.close()

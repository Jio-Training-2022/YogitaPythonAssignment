
#Question: 8 Take user input and write it to a file.

# entry = input("Enter you text.")
# with open('file.txt', "w") as f:
#   f.write(entry)


# Question 9: Fetch the data from a url and save it to a file.
# from bs4 import BeautifulSoup
# import requests

from bs4 import BeautifulSoup
import requests
URL = 'https://en.wikipedia.org/wiki/Main_Page'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
soup1 = soup.get_text()
soup1 = soup1.encode('utf-8').decode('ascii', 'ignore')
new_file = open("readme1.txt", "w")
new_file.write(soup1)
new_file.close()



#Question 10: Fetch the data from a url and calculate the number of strings in it.

data=soup1.split()
print('The number of strings is' , len(data))
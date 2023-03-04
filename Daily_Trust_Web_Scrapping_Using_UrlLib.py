from urllib.request import urlopen
from bs4 import BeautifulSoup

url1 = "https://dailytrust.com/does-tinubu-have-what-it-takes-to-rule-nigeria/"
url2 ="https://dailytrust.com/87-days-to-go-buhari-races-to-complete-legacy-projects/"

fileObj1 = urlopen(url1)
fileObj2 = urlopen(url2)

html1 = fileObj1.read()
html2 = fileObj2.read()

soup1 = BeautifulSoup(html1, 'html.parser')
soup2 = BeautifulSoup(html2, 'html.parser')

print ('Title1:\n\n',soup1.title.text)
print ('\nContent1 (this is a podcast, so only the headline was retrieved):\n\n', soup1.p.text[18:-5])

print('\nTitle2:\n\n', soup2.title.text)
txt=soup2.body.text
txt1=txt.split()[125:-94]
print ("\nContent2:\n\n", " ".join(txt1))

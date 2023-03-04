import requests
from bs4 import BeautifulSoup

url1= "https://dailytrust.com/does-tinubu-have-what-it-takes-to-rule-nigeria/"
url2="https://dailytrust.com/87-days-to-go-buhari-races-to-complete-legacy-projects/"

response1= requests.get(url1)
response2= requests.get(url2)

content1 = response1.content
content2= response2.content

soup1 = BeautifulSoup(content1, 'html.parser')
soup2 = BeautifulSoup(content2, 'html.parser')

print ('Title1:\n\n',soup1.title.text)
print ('\nContent1 (this is a podcast, so only the headline was retrieved):\n\n', soup1.p.text[18:-5])

print('\nTitle2:\n\n', soup2.title.text)
txt=soup2.body.text
txt1=txt.split()[80:-94]
print ("\nContent2:\n\n", " ".join(txt1))'
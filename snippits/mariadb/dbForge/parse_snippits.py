import os
from bs4 import BeautifulSoup

with open('Alterdatabase.xml', 'r') as f:
    files = f.read()

soup = BeautifulSoup(files, "xml")

titles = soup.find_all('Title')
descriptions = soup.find_all('Description')
codes = soup.find_all('Code')

print(f'title: {titles} \ndescription: {descriptions} \ncode: {codes}')

#%%
import os
from bs4 import BeautifulSoup

for files in os.listdir("."):
    with open(files, 'r') as f:
        file = f.read()
        
    soup = BeautifulSoup(file, "xml")
    titles = soup.find_all('Title')
    descriptions = soup.find_all('Description')
    codes = soup.find_all('Code')
    
    print(f'title: {titles} \ndescription: {descriptions} \ncode: {codes}\n\n')
# %%

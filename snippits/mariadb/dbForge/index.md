# dbForge Snippits

> Disclaimer: These snippits came with the trial installation of dbForge

## Problem: Converting `filename.snippit` into a useful format

These snippits are actually xml templates, so we'll use a simple python script to change their file extension to reflect that:

### `rename_files.py`

```py
import os

[os.rename(f, f.replace(".snippet", ".xml")) for f in os.listdir(".") if not f.startswith(".")]
```

## Parsing the XML templates into SQL snippits

```py
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
```

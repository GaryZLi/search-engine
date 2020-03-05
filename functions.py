import math
from bs4 import BeautifulSoup
import re

def strip(text):
    cur = 0
    length = len(text)
    tokens = []
    
    while cur < length:
        while cur < length and text[cur] == '\\':
            cur += 2
        
        start = cur
        
        while cur < length and text[cur] != '\\':
            cur += 1
        
        temp = text[start:cur].lower()
        
        if len(temp) > 0:
            current = 0
            end = len(temp) - 1
            
            try:
                while current < len(temp) and ord(temp[current]) < 48 or (ord(temp[current]) > 57 and ord(temp[current]) < 97) or ord(temp[current]) > 122:
                    current += 1
            
                while end >= current and ord(temp[end]) < 48 or (ord(temp[end]) > 57 and ord(temp[end]) < 97) or ord(temp[end]) > 122:
                    end -= 1
                # for key in (temp[current:end+1]):
                    # tokens.append(key)

                tokens.append(temp[current:end+1])

            except:
                pass
        
    return tokens

def tokenize(text):
    tags = ['h6', 'h1', 'a', 'div', 'p', 'a', 'all the tags']
    tokens = set()
        
    soup = BeautifulSoup(text, "html.parser")
    headers = re.compile('^h[1-9]$')
    



    for i in soup.find_all():
        if 'script' != i.name:
            for token in BeautifulSoup(str(i), 'html.parser').text.split():
                results = strip(token)

                if len(results) > 0:
                    for result in results:
                        tokens.add(result)


#                    print(strip(token))
                    # tokens.append(token.strip("\n\t\t"))
                    
                    
#        for tag in soup.find_all():
#            content = soup.find(tag.name)
#            print(tag.name, content)
#            print()
        
    return tokens
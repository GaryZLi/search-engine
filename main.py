import os
import json
from functions import *
from sys import getsizeof

import time

from timeit import timeit

start = timeit()

docStore = {}
urlStore = {}

documentName = {}
documentUrl = {}

docNum = 0

with open("output.txt", "w") as output:
    for directory in os.listdir('DEV'):
        try:
            directory = 'DEV/' + directory + '/'
            print('\n\n\n\n\n\n\n\n\n\n', directory)
            for fileName in os.listdir(directory):

                print(fileName)

                with open(directory + fileName, 'r') as file:
                    jsonResult = json.loads(file.read())

                    for token in tokenize(jsonResult['content']):

                        if token in documentName:
                            if docNum in documentName[token]:
                                documentName[token][docNum] += 1
                            else:
                                documentName[token][docNum] = 1
                        else:
                            documentName[token] = {docNum: 1}

                    

                        if token in documentUrl:
                            if docNum in documentUrl[token]:
                                documentUrl[token][docNum] += 1
                            else:
                                documentUrl[token][docNum] = 1
                        else:
                            documentUrl[token] = {docNum: 1}
                    
                    docStore[docNum] = fileName
                    urlStore[docNum] = jsonResult['url']

                    docNum += 1

            docNum += 1
        except NotADirectoryError:
            print('not a directory')

with open('documentName', 'a') as file:
    file.write(json.dumps(documentName))

with open('documentUrl', 'a') as file:
    file.write(json.dumps(documentUrl))

with open('docStore', 'a') as file:
    file.write(json.dumps(docStore))

with open('urlStore', 'a') as file:
    file.write(json.dumps(urlStore))

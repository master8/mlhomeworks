import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import os
import urllib.parse

import time

start = time.time()

files = os.listdir('raw')
files_name = [name[:-5] for name in files]

names_and_index = {}

i = 0
for n in files_name:
    names_and_index[n] = i
    i += 1

matrix = np.zeros((len(files_name), len(files_name)))

k = 0
soup = None
for file in files:
    with open('raw/' + file) as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

        a = soup.find_all('a')
        hrefs = [a.get('href') for a in soup.find_all('a')]

        results = []
        for h in hrefs:
            if h is not None and h.startswith('/wiki/'):
                results.append(h[6:])

        hrefs = results
        h = hrefs[0]
        h.startswith('/wiki/')

        hrefs = list(set(hrefs))
        hrefs = [urllib.parse.unquote(h) for h in hrefs]

        for h in hrefs:
            if h in files_name:
                matrix[k][names_and_index[h]] = 1

        # print(str(k))
        k += 1


end = time.time() - start
print(end)


for i in range(0, len(files_name)):
    for j in range(0, len(files_name)):
        if matrix[i][j] == 0:
            matrix[i, j] = 0.001

row_sum = matrix.sum(axis=1)
matrix_prob = matrix / row_sum[:, np.newaxis]

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

vector = np.array([0.2]*len(files_name))

for i in range(100):
    prev_vector = vector
    vector = matrix_prob.transpose().dot(vector)
    # print(str(i) + ' ' + str((np.abs(prev_vector - vector).sum())))


rank = {}

for i, value in enumerate(vector):
    rank[i] = value


# all
print()
print("all")
print()

new_rank = rank.copy()

items = sorted(new_rank.items(), key=lambda t: t[1])[::-1][:n]
for index, value in items:
    print(files_name[index] + ' ' + str(value))

# армстронг
word = "армстронг"

print()
print(word)
print()

page_with_word = []

for i, name in enumerate(files_name):
    if word.lower() in name.lower():
        page_with_word.append(i)

new_rank = {}
for i in page_with_word:
    new_rank[i] = rank[i]

items = sorted(new_rank.items(), key=lambda t: t[1])[::-1][:n]
for index, value in items:
    print(files_name[index] + ' ' + str(value))
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import os
import urllib.parse

import time
import scipy
import scipy.linalg

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


word = "армстронг"

page_with_word = []

for i, name in enumerate(files_name):
    if word.lower() in name.lower():
        page_with_word.append(i)

base_set = page_with_word.copy()

for i in page_with_word:
    for j in range(0, len(files_name)):
        if matrix[i][j] > 0:
            base_set.append(j)

    for j in range(0, len(files_name)):
        if matrix[j][i] > 0:
            base_set.append(j)

base_set = list(set(base_set))

a = np.zeros((len(base_set), len(base_set)))

for i in range(0, len(base_set)):
    for j in range(0, len(base_set)):
        a[i, j] = matrix[base_set[i]][base_set[j]]

at = a.transpose()

aat = a.dot(at)
ata = at.dot(a)

hub = np.abs(np.linalg.eigh(aat)[1]).sum(axis=1)
auth = np.abs(np.linalg.eigh(ata)[1]).sum(axis=1)

print()
print("hub")
print()

dhub = {}

for i, value in enumerate(hub):
    dhub[i] = value

n = 10

dbase = {}
for i, value in enumerate(base_set):
    dbase[value] = i

new_dhub = {}
for i in page_with_word:
    new_dhub[dbase[i]] = dhub[dbase[i]]

items = sorted(new_dhub.items(), key=lambda t: t[1])[::-1][:n]
for index, value in items:
    print(files_name[base_set[index]] + ' ' + str(value))


print()
print("auth")
print()

dauth = {}

for i, value in enumerate(auth):
    dauth[i] = value

new_dauth = {}
for i in page_with_word:
    new_dauth[dbase[i]] = dauth[dbase[i]]

items = sorted(new_dauth.items(), key=lambda t: t[1])[::-1][:n]
for index, value in items:
    print(files_name[base_set[index]] + ' ' + str(value))


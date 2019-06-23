from bs4 import BeautifulSoup
import requests
import datetime
import pandas as pd
import numpy as np

from tqdm import tqdm

tqdm.pandas()

import random
import time

from sklearn.metrics import jaccard_score

import pandas as pd
import numpy as np

from collections import Counter

from sklearn.decomposition import TruncatedSVD

import pickle


# https://lenta.ru/news/2019/05/30/
#
# https://russian.rt.com/listing/type.News/prepare/all-news/15/0

co = pd.read_csv('news_rt.csv')
co = pd.read_pickle('news_all.pkl')

def download_text(href: str):
    time.sleep(1 / random.randint(1, 10))
    try:
        r = requests.get('https://russian.rt.com' + href)
        if r.status_code != 200:
            print('error: ' + str(r.status_code))
            return 'error_r'
        else:
            return ' '.join(
                [p.text for p in
                 BeautifulSoup(r.text, 'html.parser').find('div', class_='article__text').find_all('p')])
    except:
        return 'error'



def download_text_lenta(href: str):
    time.sleep(1 / random.randint(1, 10))
    try:
        r = requests.get('https://lenta.ru' + href)
        if r.status_code != 200:
            print('error: ' + str(r.status_code))
            return 'error_r'
        else:
            return ' '.join([p.text for p in BeautifulSoup(r.text, 'html.parser').find('div', class_='b-text').find_all('p')])
    except:
        return 'error'

co['text'] = co.href.progress_apply(download_text_lenta)

co = pd.read_csv('news_all.csv')

from string import ascii_lowercase, digits, whitespace
cyrillic = u"абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
allowed_characters = ascii_lowercase + digits + cyrillic + whitespace

# text = np.array(co[:1].text)[0]
#
# clean_text = ''.join([character if character in set(allowed_characters) else ' ' for character in text.lower()])
# clean_text = ' '.join(clean_text.split())
# splited_text = clean_text.split()
# symbols = list(clean_text)


def clean_text(text: str):
    clean_text = ''.join([character if character in set(allowed_characters) else ' ' for character in text.lower()])
    return ' '.join(clean_text.split())

co['clean_text'] = co.text.progress_apply(clean_text)


n = 2

def build_shingles(list):
    shingles = []
    for i in range(0, len(list) - n + 1):
        shingle = []
        for j in range(0, n):
            shingle.append(list[i + j])
        shingles.append(' '.join(shingle))
    return shingles

co['shingles_2'] = co.words.progress_apply(build_shingles)

bag_of_shingles = []
for shingles in co.shingles_2:
    bag_of_shingles.extend(shingles)

bag_of_shingles = set(bag_of_shingles)
bag_of_shingles = list(bag_of_shingles)

# def build_vector(shingles):
#     return [int(shingle in shingles) for shingle in bag_of_shingles]

bag_dic = {}

for i in range(0, len(bag_of_shingles)):
    bag_dic[bag_of_shingles[i]] = i

# def build_vector(shingles):
#     r = [0] * len(bag_of_shingles)
#     for shingle in shingles:
#         r[bag_of_shingles.index(shingle)] = 1
#     return r

def build_vector(shingles):
    r = [0] * len(bag_of_shingles)
    for shingle in shingles:
        r[bag_dic[shingle]] = 1
    return r

co['vectors'] = co.shingles_2.progress_apply(build_vector)
vectors = np.array(co.vector).tolist()


# jaccard_score([], [], average='micro')


index = {}

for shingle in bag_of_shingles:
    index[shingle] = []

i = 0
for shingles in np.array(co.shingles_2):
    for shingle in shingles:
        index[shingle].append(i)
    i += 1





def count_sim(shingles):
    result = []

    for sh in shingles:
        result.extend(index[sh])

    result_count = Counter(result)
    min = np.max(list(result_count.values())) * 0.5

    result = []

    for key, value in result_count.items():
        if value > min:
            result.append(key)

    return len(result) - 1


def get_sim(id):
    result = []

    for sh in np.array(co[co.id == id].shingles_2)[0]:
        result.extend(index[sh])

    result_count = Counter(result)
    min = np.max(list(result_count.values())) * 0.5

    result = []

    for key, value in result_count.items():
        if value > min and key != id:
            result.append(key)

    sim = {}
    v1 = vc[id]
    for i in result:
        v2 = vc[i]
        sim[i] = jaccard_score(v1, v2, average='micro')

    return sim




import pickle
file = open('news_csr.pkl', 'rb')
vc = pickle.load(file)
file.close()

# sim = []
# v1 = vc[0]
# for i in result:
#     v2 = vc[i]
#     sim.append(jaccard_score(v1, v2, average='micro'))


co['count_sim'] = co.shingles_2.progress_apply(count_sim)
co_sim = co[co.count_sim > 0]

co_sim_1 = co_sim[co_sim.count_sim == 1]
co_sim_1['sim'] = co_sim_1.id.progress_apply(get_sim)
co_sim_1['sim_value'] = co_sim_1.sim.apply(lambda x: list(x.values())[0])
co_sim_1 = co_sim_1.sort_values(['sim_value'], ascending=False)
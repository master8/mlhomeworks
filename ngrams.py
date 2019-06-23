import numpy as np
import pandas as pd

import random

from tqdm import tqdm

tqdm.pandas()

co = pd.read_pickle('news_all.pkl')

all_texts = np.array(co.shingles_2)

bigram_frequency = {}

for text in all_texts:
    for bigram in text:
        if bigram in bigram_frequency:
            bigram_frequency[bigram] = bigram_frequency[bigram] + 1
        else:
            bigram_frequency[bigram] = 1

model = pd.DataFrame()
model['bigram'] = bigram_frequency.keys()
model['count'] = bigram_frequency.values()
model['first'] = model.bigram.apply(lambda x: x.split(' ')[0])
model['second'] = model.bigram.apply(lambda x: x.split(' ')[1])

first_count = model['first'].value_counts()
model.index = model['first']
model['first_count'] = first_count

freq = []
for index, row in tqdm(model.iterrows()):
    freq.append(row['count']/row['first_count'])

model['freq'] = freq

model.index = range(0, model.bigram.count())
model = model.sort_values(['first', 'freq'], ascending=False)
model_dict = dict(np.array(model[['bigram', 'freq']]))


sample = 'В этой дисциплине первое место тоже заняла Кинг'

n = 2

def build_shingles(list):
    shingles = []
    for i in range(0, len(list) - n + 1):
        shingle = []
        for j in range(0, n):
            shingle.append(list[i + j])
        shingles.append(' '.join(shingle))
    return shingles

sample_bigrams = build_shingles(sample.lower().split(' '))

p = 1

for bigram in sample_bigrams:
    p = p * model_dict[bigram]


word = 'президент'

def get_next_words(word: str):
    for index, row in model[model['first'] == word][:10].iterrows():
        print(str(row['second']) + ' ' + str(row['freq']))


def generate_text(start_word: str, count_words: int):
    word = start_word
    sentense = word
    n = count_words
    for _ in range(0, n):
        ring = []
        for index, row in model[model['first'] == word][:10].iterrows():
            for _ in range(0, int(row['freq'] * 1000)):
                ring.append(row['second'])

        next_word = ring[random.randint(0, len(ring) - 1)]
        sentense += ' ' + next_word
        word = next_word

    print(sentense)
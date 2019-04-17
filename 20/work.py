from functools import reduce

INPUT_FILE = 'republic.txt'

def freq(word):
    raw = ''
    with open(INPUT_FILE) as f:
        raw = f.read().lower()
    return len([x for x in raw.split() if x == word.lower()])

def group_freq(words):
    raw = ''
    with open(INPUT_FILE) as f:
        raw = f.read().lower()
    return len([x for x in raw.split() if x in map(lambda x: x.lower(), words)])

def most_freq():
    raw = ''
    with open(INPUT_FILE) as f:
        raw = f.read().lower()
    d = {}
    for word in raw.split():
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    l = []
    for word in d:
        l.append((word, d[word]))
    return sorted(l, key=lambda x: x[1], reverse=True)[:20]

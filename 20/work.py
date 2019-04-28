from functools import reduce

INPUT_FILE = 'republic.txt'

def freq(word):
    raw = ''
    with open(INPUT_FILE) as f:
        raw = f.read().lower()
    return reduce(lambda x, y: x + 1 if y == word else x,\
                  raw.split(),\
                  0)
    

def group_freq(phrase):
    raw = ''
    with open(INPUT_FILE) as f:
        raw = f.read().lower()
    return reduce(lambda x, y: x + 1 if raw[y:y+len(phrase)] == phrase else x,\
                  range(len(raw) - len(phrase)),\
                  0)

def add_one(d, word):
    d[word] += 1
    return d

def most_freq():
    raw = ''
    with open(INPUT_FILE) as f:
        raw = f.read().lower()
    d =  reduce(lambda x, y: add_one(x, y), raw.split(), dict.fromkeys(set(raw.split()), 0))
    return sorted([(x, d[x]) for x in d], key=lambda x: x[1], reverse=True)[0]
    #return reduce(lambda x, y: (y, d[y]) if d[y] > x[1] else x,\
    #              d,\
    #              ('', -1))[0]

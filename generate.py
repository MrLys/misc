# -*- coding: utf-8 -*-
import secrets
import string

def get_words(loc):
    with open(loc) as f:
        return [word.strip() for word in f]

def generate_phrase(n=0):
    w_loc = '/usr/share/dict/words'
    a_loc = 'complete_list.txt'
    satisfied = False
    words = get_words(w_loc)
    adjs = get_words(a_loc)
    if n == 0:
        while not satisfied:
            word = secrets.choice(words)
            adj = secrets.choice(adjs)
            satisfied = not (word in adjs)
        print(adj + " " + word)
    else:
        n = n-1
        while not satisfied:
            word = secrets.choice([i for i in words if len(i) <= n/2.0])
            adj = secrets.choice([i for i in adjs if len(i) <= n/2.0])
            satisfied = (not (word in adjs) and (len(word) + len(adj)) <=n)
        print(adj + " " + word)
        print(len(adj+word)+1)

if __name__ == '__main__':
    generate_phrase(18)

#! /usr/bin/python3

UC_LETTERS = {'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'}
LC_LETTERS = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'}
NUMS = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
OTHERS = {'.', '?', '!', '&', '#', ',', ';', ':', '-', '_', '*'}

def check(password):
    v = [1 if x in UC_LETTERS else 2 if x in LC_LETTERS else 3 if x in NUMS else 0 for x in password]
    return 1 in v and 2 in v and 3 in v    

def strength(password):
    v = [1 if x in LC_LETTERS else 2 if x in UC_LETTERS else 3 if x in NUMS else 4 if x in OTHERS else 0 for x in password]
    d = 7
    if 1 in v: d -= 1
    if 2 in v: d -= 1
    if 3 in v: d -= 1
    if 4 in v: d -= 1
    return min(sum(v) / d, 10)

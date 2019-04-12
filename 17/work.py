#! /usr/bin/python3

'''
Team PP
Derek Chan, Joan Chirinos
SoftDev2 pd08
K17 -- 
2019-04-12
'''

#1a
a1 = []
for i in range(0, 9, 2):
    a1.append(str(i)*2)
print('1a: {}'.format(a1))

#1b
b1 = [str(i)*2 for i in range(0, 9, 2)]
print('1b: {}\n'.format(b1))

#2a
a2 = []
for i in range(5):
    a2.append(i*10 + 7)
print('2a: {}'.format(a2))

#2b
b2 = [i*10 + 7 for i in range(5)]
print('2b: {}\n'.format(b2))

#3a

#3b

#4a
a4 = []
for i in range(0, 100+1):
    for j in range(2, i):
        if i % j == 0:
            a4.append(i)
            break
print('4a: {}'.format(a4))

#4b
b4 = [i for i in range(2, 101) if True in [True if i % j == 0 else False for j in range(2, i)]]
print('4b: {}\n'.format(b4))

#5a
a5 = []
for i in range(2,100+1):
    val = True
    for j in range (2,i):
        if i % j == 0:
            val = False
            break
    if val:
        a5.append(i)
print('5a: {}'.format(a5))


#5b
b5 = [i for i in range(2, 101) if True not in [True if i % j == 0 else False for j in range(2, i)]]
print('5b: {}\n'.format(b5))

#6a
def divisors(i):
    out = []
    for j in range(1, i+1):
        if i % j == 0:
            out.append(j)
    return out
a6 = divisors(120)
print('6a: {}'.format(a6))

#6b
def divisors_lc(i):
    return [j for j in range(1, i+1) if i % j == 0]
b6 = divisors(120)
print('6b: {}\n'.format(b6))

#7a
def transpose(m):
    out=[]
    for i in range(len(m[0])):
        a = []
        for j in range(len(m)):
            a.append(m[j][i])
        out.append(a)
    return out

a7 = transpose([[1,2,3],[4,5,6]])
print('7a: {}'.format(a7))




















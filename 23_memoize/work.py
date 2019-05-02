import random, time, sys

sys.setrecursionlimit(1000000000)

def make_HTML_heading(f):
    def inner():
        return '<h1>' + f() + '</h1>'
    return inner

# equivalent to greet = make_HTML_heading(greet)
@make_HTML_heading
def greet():
    greetings = ['Hello', 'Welcome', 'AYO!', 'Hola', 'Bonjour', 'Word up']
    return random.choice(greetings)

def naive_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return naive_fib(n - 1) + naive_fib(n - 2)

def memoize(f):
    memo = dict()
    def helper(x):
        if x in memo:
            return memo[x]
        bean = f(x)
        memo[x] = bean
        return bean
    return helper

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

s = time.time()
print(fib(12000))
print(time.time() - s, '\n')

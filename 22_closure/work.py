def repeat(word):
    def times(n):
        print(n*word)
    return times

def foo():
    def boo():
        def roo():
            def loo():
                def koo():
                    def too():
                        def woo():
                            def goo():
                                print('hah')
                            return goo()
                        return woo
                    return too
                return koo
            return loo
        return roo
    return boo

r1 = repeat('hello')
r2 = repeat('goodbye')

r1(2)
r2(2)
repeat('cool')(3)


def make_counter():
    x = 0
    def inc():
        nonlocal x
        x += 1
        return x
    def get():
        nonlocal x
        return x
    return inc, get

inc1, get1 = make_counter()

print(inc1())
print(inc1())
print(inc1())
print(get1())
print(inc1())
print(get1())
print(get1())

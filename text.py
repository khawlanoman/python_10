from functools import partial

def mul(a,b):
    return a*b
d = partial(mul,3)
d(5)
print(d.func)
print(d.args)
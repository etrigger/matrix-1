# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec



## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    u = list2vec([ randGF2() for i in range(6)])
    while ( not (a0*u == s and b0*u == t)):
        u = list2vec([ randGF2() for i in range(6)])
    return u
   



## Problem 2
# Give each vector as a Vec instance
from vec import Vec
secret_a0 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: one, 4: 0, 5: one})
secret_b0 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: 0, 4: 0, 5: one})
secret_a1 = ...
secret_b1 = ...
secret_a2 = ...
secret_b2 = ...
secret_a3 = ...
secret_b3 = ...
secret_a4 = ...
secret_b4 = ...


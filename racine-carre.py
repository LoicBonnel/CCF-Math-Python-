# sqrt(a) = Square roots = racine carré

from __future__ import division
from lycee import *

def hyp(a,b):
    c=sqrt(a**2+b**2)
    return c
print (hyp(3,4))
def per(a,b):
    p = a+b+hyp(a,b)
    return p
print (per(3,4))

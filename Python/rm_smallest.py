from cgitb import small
from optparse import Values
import sys


def rm_smallest(d):
    # Your code here!
    small = sys.maxsize 
    skey = sys.maxsize 

    if d == {}:
        return d
    else:
        for key in d: 
            if d[key] < small:
                small = d[key]
                skey = key 
        del d[skey] 
    return d;

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()

import re
import time
import random
import math

class A(object):
    def __init__(self):
        print("entering A ")
        super().__init__()
        print("exiting A ")
class B(A):
    def __init__(self):
        print("entering B ")
        super().__init__()
        print("exiting B ")
class C(object):
    def __init__(self):
        print("entering C ")
        super().__init__()
        print("exiting C ")
class D(object):
    def __init__(self):
        print("entering D ")
        super().__init__()
        print("exiting D ")
class E(B,C,D):
    def __init__(self):
        print("entering E ")
        super().__init__()
        print("exiting E ")

class SortedTuple(tuple):

    instances_created = 0
    def __new__(cls, *args):
        instance = tuple.__new__(cls, sorted(*args))
        instance.non_zero = sum(1 for i in instance if i != 0)
        SortedTuple.instances_created += 1
        return instance
    
    def differences(self):
        differenc = ()
        for i in range(1,len(self)):
            differenc += (self[i] - self[i-1],)
        return differenc
    
def dup1_with_given_key(iterable, key=str):
    seen_keys = set()
    seen_elements = set()
    elements_with_same_key = set() # save items that have the same key but havent been seen yet

    for item in iterable:
        current_key = key(item)
        if current_key in seen_keys:
            if current_key not in seen_elements:
                yield item
                seen_elements.add(current_key)
        else:
            seen_keys.add(current_key)
            elements_with_same_key.add(current_key)
    return elements_with_same_key

def limit_calls(max_calls, message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                if wrapper.calls >= max_calls:
                    raise Exception(message)
                wrapper.calls += 1
                return func(*args, **kwargs)
            except Exception as e:
                return f"__main__.TooManyCallsError: function pyth - {e}"
        wrapper.calls = 0
        return wrapper
    return decorator



@limit_calls(1,'that is too much')
def pyth(a,b):
    c = math.sqrt(a**2 + b**2)
    return c

def main():
    camel_re = r'(?<=[a-z])(?=[A-Z])'
    fruits = 'AppleOrangeBananaStrawberryPeach'
    print(re.sub(camel_re, ' ',fruits))
    #2
    words = ('flower','foe','flights')
    for i in zip(*words):
        print(i)
    #3
    e = E()
    #4
    dict1 = {
    (1, 'b', 'C'): [1, 2],
    (2, 'A', 'c'): [2, 3],
    (3, 'c', 'd'): [0, 0, 0],
    (4, 'e', 'b'): [2, 3],
    (2, 'a', 'b'): [2, 3]
    }
    dict1 = sorted(dict1.items(),key=lambda item: (
        len(item[1]),                                 # podle délky seznamu (vzestupně)
        -ord(item[0][2].lower()),                     # podle 3. prvku trojice (sestupně, case-insensitive)
        -ord(item[0][1].lower())                      # podle 2. prvku trojice (sestupně, case-insensitive)
    ))
    print(dict1)
    #5
    st = SortedTuple(k*11 for k in (3,0,1,0,2))
    print(st)
    print(list(st.differences()))
    #6
    print(tuple(dup1_with_given_key([[1],[2,3],[4],[5,6,7],[8,9]],len)))
    print(tuple(dup1_with_given_key([[2,3],[4],[1],[4],[2,3]])))
    #7
    print(pyth(3,4))
    print(pyth(6,8))


if __name__ == "__main__":
    main()


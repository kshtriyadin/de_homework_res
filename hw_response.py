1) Ans:-

Approach 1:-

import sys

def func(a, b):
    l1, l2 = len(a), len(b)
    mn = sys.maxsize
    lst = []
    for i in range(l1):
        for j in range(l2):
            dif = abs(a[i] - b[j])
            mn = min(mn, dif)
            print(a[i], b[j], mn, dif)
            if dif <= mn:
                lst.clear()
                lst.append(a[i])
                lst.append(b[j])

    return lst


print(func([47,24,95,184,15,3,12,18],[83,9,32,29,52,90,108,14]))

'''
a = [47,24,95,184,13,3,12,18]
b = [83,9,32,29,52,90,108,14]  '''


O(1000*1000)


Approach 2:-


import sys


def func(a, b):
    lst1 = sorted(a)
    lst2 = sorted(b)
    lst = []
    l1 = l2 = 0
    mn = sys.maxsize

    while l1 < len(a) and l2 < len(b):
        dif = lst1[l1] - lst2[l2]
        if mn > abs(dif):
            lst.clear()
            lst.append(lst1[l1])
            lst.append(lst2[l2])
        mn = min(abs(dif), mn)
        #print(lst1[l1], lst2[l2], mn, abs(dif))
        #print('lst:' ,  lst, mn)
        if dif < 0:
            l1 += 1
        else:
            l2 += 1
    return mn, lst
    


print(func([47,24,95,184,15,3,12,18],[83,9,32,29,52,90,108,14]))

    O(max(1000*log(1000), 1000*log(100))
    
-----------------------------------------------------------------------------------------------------------------------------------------------

2) ''' Approach 2 will perform better that 1 as complexity is less in 2nd approach.
    Big0 notationO:Approach 1
    (1000*1000)

    Big0 notationO:Approach 2
    O(max(1000*log(1000), 1000*log(100))'''
    
    
    
  Approach 1:-  
    
    
import random
import sys


def func(a, b):
    l1, l2 = len(a), len(b)
    mn = sys.maxsize
    lst = []
    for i in range(l1):
        for j in range(l2):
            dif = abs(a[i] - b[j])
            mn = min(mn, dif)
            print(a[i], b[j], mn, dif)
            if dif <= mn:
                lst.clear()
                lst.append(a[i])
                lst.append(b[j])

    return lst, mn


lst1 = []
lst2 = []
for i in range(1, 1000):
    n = random.randint(1, 10000000)
    m = random.randint(1, 10000000)
    lst1.append(n)
    lst2.append(m)
print(lst1, lst2)
print(func(lst1, lst2))



  Approach 2:- 



import random
import sys


def func(a, b):
    lst1 = sorted(a)
    lst2 = sorted(b)
    lst = []
    l1 = l2 = 0
    mn = sys.maxsize

    while l1 < len(a) and l2 < len(b):
        dif = lst1[l1] - lst2[l2]
        if mn > abs(dif):
            lst.clear()
            lst.append(lst1[l1])
            lst.append(lst2[l2])
        mn = min(abs(dif), mn)
        #print(lst1[l1], lst2[l2], mn, abs(dif))
        #print('lst:' ,  lst, mn)
        if dif < 0:
            l1 += 1
        else:
            l2 += 1
    return mn, lst


lst1 = []
lst2 = []
for i in range(1, 1000):
    n = random.randint(1, 10000000)
    m = random.randint(1, 10000000)
    lst1.append(n)
    lst2.append(m)
print(lst1, lst2)
print(func(lst1, lst2))

-----------------------------------------------------------------------------------------------------------------------------------------------
'''
Conceptually, what are the different tools such as code libraries or infrastructure that could help you find the smallest non-negative difference between 1 million lists that are 5,000 integers long?

We cab use NumPy, SciPy, Keras & Teano libraries to utilize their in-built methods for big computation '''
#!/usr/bin/env python
# coding: utf-8

# In[2]:


def solution():
    f = open("demofile.txt", "r")
    print(f.readline())


# In[95]:


rt = ''
contents ={}
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    num = int(lines[-1])
for line in lines[:-1]:
    n, s = line.split(':')
    
def sort(num,lines):
    mid = len(lines)//2
    if len(lines) == 0:
        return ''
    elif len(lines) == 1:
        n, s = lines[0].split(':')
        if num%int(n) == 0:
            return [[int(n), s]]
        else:
            return ''
    else:
        left = sort(num,lines[:mid])
        right = sort(num,lines[mid:])
        return merge(left, right)

def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j][0] < b[h][0]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c

re = sort(num, lines[:-1])

if len(re) > 0:
    string = ''
    for i in re:
        string += i[1]
    print(string)
else:
    print(num)


# In[67]:


def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


# In[97]:


def sort(num,lines):
    mid = len(lines)//2
    if len(lines) == 0:
        return ''
    elif len(lines) == 1:
        n, s = lines[0].split(':')
        if num%int(n) == 0:
            return [[int(n), s]]
        else:
            return ''
    else:
        left = sort(num,lines[:mid])
        right = sort(num,lines[mid:])
        return merge(left, right)

def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j][0] < b[h][0]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def solution():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        num = int(lines[-1])
    for line in lines[:-1]:
        n, s = line.split(':')
    re = sort(num, lines[:-1])

    if len(re) > 0:
        string = ''
        for i in re:
            string += i[1]
        return(string)
    else:
        return(num)

solution()


# In[64]:


if not 's':
    print(True)


# In[ ]:





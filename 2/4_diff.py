#!/usr/bin/python

import sys


def diff(f1, f2):

    def backtrace():
        f1.seek(0)
        f2.seek(0)
        for x in path:
            if x == 0:
                print(f'    {f1.readline()}', end='')
                f2.readline()
            elif x == 1:
                print('\033[91m' + f'--- {f1.readline()}' + '\033[0m', end='')
            else:
                print('\033[92m' + f'+++ {f2.readline()}' + '\033[0m', end='')
        return

    def add_to_queue(i, j, dir_=0):
        nonlocal queue, path_queue
        p = path[:]
        p.append(dir_)
        if not dir_:
            queue.insert(0, (i, j))
            path_queue.insert(0, p)
        else:
            queue.append((i, j))
            path_queue.append(p)
   
    hash1 = [hash(x) for x in f1]  
    hash2 = [hash(x) for x in f2]
    len1 = len(hash1) 
    len2 = len(hash2) 
    
    queue = [(0, 0)]
    path_queue = [[]]
    visited = [0] * (len1 * len2)
    while queue:
        i, j = queue.pop(0)
        path = path_queue.pop(0)
        
        if visited[i * len1 + j]:
            continue
        visited[i * len1 + j] = 1
        
        if i == len1 and j == len2:
        #     print(path)
            backtrace()

        if i < len1 and j < len2 and hash1[i] == hash2[j] and not visited[(i + 1) * len1 + j + 1]:
            add_to_queue(i + 1, j + 1)
        else:
            if i < len1 and not visited[(i + 1) * len1 + j]:
                add_to_queue(i + 1, j, 1)
            if j < len2 and not visited[i * len1 + j + 1]:
                add_to_queue(i, j + 1, 2)


# with open('./4_1.txt') as f1, open('./4_2.txt') as f2:
with open(sys.argv[1]) as f1, open(sys.argv[2]) as f2:
    diff(f1, f2)




#!/usr/bin/python

from random import shuffle

def mine_field(row,col,count):
    count = row*col if count>row*col else count
    g = [i for i in range(row*col)]
    shuffle(g)
    grid = [[0 for j in range(col+2)] for i in range(row+2)]
    for cell in g[:count]:
        r,c = cell/row+1,cell%col+1
        grid[r][c] = 'M'
        for i in range(-1,2):
            for j in range(-1,2):
                if (i or j) and grid[r+i][c+j] != 'M':
                    grid[r+i][c+j] += 1
    return [[c for c in r[1:-1]] for r in grid[1:-1]]

if __name__ == '__main__':
    for r in mine_field(15,15,20):
        print ' '.join([str(c) for c in r])

#!/usr/bin/env python

def ManhattanTourist(n, m, down_matrix, right_matrix):
    '''
    Solve Manhattan Tourist Problem via dynamic programming (h&v only)
    '''

    mht_dic = {(0,0):0}

    for i in range(1, n):
        mht_dic[(i,0)] = mht_dic[(i-1,0)] + down_matrix[i-1][0]

    for j in range(1, m):
        mht_dic[(0,j)] = mht_dic[(0,j-1)] + right_matrix[0][j-1]

    # calulating
    for i in range(1, n):
        for j in range(1,m):
            mht_dic[(i,j)] = max(mht_dic[(i-1,j)]+down_matrix[i-1][j], mht_dic[(i,j-1)] + right_matrix[i][j-1])

    return mht_dic[(n-1,m-1)]

if __name__ == "__main__":
    # Read the input data
    import sys
    data = sys.stdin

    line=data.readline().rstrip('\n')
    down_matrix= []
    while (line != '---'):
            if line.startswith('G'):
                    line = data.readline().rstrip('\n')
            else:
                    down_matrix.append([float(i) for i in line.split('   ')])
                    line=data.readline().rstrip('\n')
    if line == '---':
            line = data.readline().rstrip('\n')

    right_matrix= []
    while (line != '---'):
            if line.startswith('G'):
                    line = data.readline().rstrip('\n')
            else:
                    right_matrix.append([float(i) for i in line.split('   ')])
                    line=data.readline().rstrip('\n')

    n= int(len(down_matrix[0]))
    m= int(len(right_matrix))

    if n != m or len(down_matrix) != len(right_matrix[0]):
        print("Fehler bei Einlesen von Datei")
    else:
        max_dist = ManhattanTourist(n,m,down_matrix,right_matrix)
        print (max_dist)

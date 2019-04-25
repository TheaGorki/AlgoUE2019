#!/usr/bin/python

#Algorithmen_Aufgabe5_ADGorki_NeedlemanWunschAlgo
from Bio import SeqIO
import argparse
import numpy as np

parser = argparse.ArgumentParser(description="Needleman-Wunsch pairwise global sequence alignment")
parser.add_argument("--match", type=int, help="integer number for match", default= 1)
parser.add_argument("--mismatch", type=int, help="integer number for mismatch", default= -1)
parser.add_argument("--gap", type=int, help="integer number for gap", default= -2)
args = parser.parse_args()

def substring(s, offset=None, length=None):
    return s[offset:][:length]

def Score(a, b):
    if a == b:
        return match
    elif a == "-" or b == "-":
        return gap
    else:
        return mismatch

def NeedlemanWunsch(sequence1, sequence2, gap):
    '''
    Solve global alignment via Needleman Wunsch algorithm
    '''

    n= len(sequence1)
    m= len(sequence2)
    num_row = n + 1
    num_col = m + 1

    scoring_matrix= np.zeros(shape=(num_row, num_col), dtype=np.int)

    for i in range(0,num_row):
        scoring_matrix[i][0] = gap * i

    for j in range(0,num_col):
        scoring_matrix[0][j] = gap * j

    scoring_matrix[0][0] = 0
    for i in range(1,num_row):
        for j in range(1, num_col):
            match_score = scoring_matrix[i-1][j-1] + Score(sequence1[i-1], sequence2[j-1])
            delete_score = scoring_matrix[i-1][j] + gap
            insert_score = scoring_matrix[i][j-1] + gap
            scoring_matrix[i][j] = max(match_score, delete_score, insert_score)
    print("%s \n" %(scoring_matrix[n][m]), file= sys.stderr)

    trace1= ''
    trace2= ''
    i, j = n, m
    while i > 0 and j > 0:
        scoring_atm = scoring_matrix[i][j]
        scoring_dia = scoring_matrix[i - 1][j - 1]
        scoring_up = scoring_matrix[i][j - 1]
        scoring_vert = scoring_matrix[i - 1][j]

        if scoring_atm == scoring_dia + Score(sequence1[i - 1], sequence2[j - 1]):
            trace1 += sequence1[i - 1]
            trace2 += sequence2[j - 1]
            i -= 1
            j -= 1
        elif scoring_atm == scoring_vert + gap:
            trace1 += sequence1[i - 1]
            trace2 += '-'
            i -= 1
        elif scoring_atm == scoring_up + gap:
            trace1 += '-'
            trace2 += sequence2[j - 1]
            j -= 1

    while i > 0:
        trace1 += sequence1[i - 1]
        trace2 += '-'
        i -= 1
    while j > 0:
        trace1 += '-'
        trace2 += sequence2[j - 1]
        j -= 1

    trace_A= trace1[::-1]
    trace_B= trace2[::-1]

    print_out= ''

    for i in range(len(trace_A)):
        if trace_A[i] == trace_B[i]:
            print_out= print_out + "*"
        else:
            print_out= print_out + " "

    return {"trace_Seq1":trace_A, "trace_Seq2":trace_B, "alignment":print_out}


if __name__ == "__main__":
    # Read the input data
    import sys
    import re
    data = sys.stdin

    #Write headers in one list, sequences in other list
    HeaderList = []
    SequenceList= []
    for record in SeqIO.parse(data,'fasta'):
        HeaderList.append(record.id)
        SequenceList.append(str(record.seq))

    Sequence1= SequenceList[0]
    Sequence2= SequenceList[1]

    match = args.match
    mismatch = args.mismatch
    gap = args.gap

    result= NeedlemanWunsch(Sequence1, Sequence2, gap)

    HeaderList_ID=[]
    for i in range(len(HeaderList)):
        s=HeaderList[i]
        HeaderList_ID= HeaderList_ID + s.split(" ",1)

    x= " "
    a= result['trace_Seq1']
    b= result['trace_Seq2']
    c= result['alignment']

    maximum = int(max(len(a),len(b),len(c))/40) + (max(len(a),len(b),len(c))%40 >0)

    for i in range(maximum):
        print(HeaderList_ID[0], 5 * x, substring(a, i * 40, (i + 1) * 40))
        print(HeaderList_ID[1], 5 * x, substring(b, i * 40, (i + 1) * 40))
        print((len(HeaderList_ID[1])+6) * x, substring(c, i * 40, (i + 1) * 40))
        i = i + 1




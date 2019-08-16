#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    res = [1 for i in range(alice_count+1)]
    i = alice_count-1
    j = 0

    while i>=0:
        if alice[i]>=scores[j]:
            i-=1
            res[i] = res[i+1]
            while (alice[i]==alice[i+1]):
                i-=1
                if i<0:
                    break
                res[i] = res[i+1]
                
        else:
            res[i]+=1
            j+=1
            while scores[j]==scores[j-1]:
                j+=1
    del res[alice_count]
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())+1

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))
    scores.append(0)

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

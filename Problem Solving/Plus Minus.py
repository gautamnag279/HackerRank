#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negetive = 0
    neutral = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            positive = positive + 1
        if arr[i] == 0:
            neutral = neutral + 1
        if arr[i] < 0:
            negetive = negetive + 1
    print(positive/len(arr))
    print(negetive/len(arr))
    print(neutral/len(arr))
            
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

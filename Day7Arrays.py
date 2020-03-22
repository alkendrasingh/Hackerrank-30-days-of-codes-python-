import math
import os
import random
import re
import sys




n = int(input())

arr = list(map(int, input().rstrip().split()))
reversed_array=[]
for i in range(n):
    reversed_array.append(arr[n-i-1])

Output_string=''
for i in range(len(reversed_array)):
    Output_string+=str(reversed_array[i])+' '

print(Output_string)

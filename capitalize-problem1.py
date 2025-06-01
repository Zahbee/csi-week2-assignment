#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    # Split the input string 's' by spaces.
    words = s.split(' ')
    
    capitalized_words = []
    for word in words:
        # Apply the .capitalize() method to each "word".
        capitalized_words.append(word.capitalize())
            
    # Join the processed words back together with a single space.
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

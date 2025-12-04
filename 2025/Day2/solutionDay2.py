############################################################################################
######################################### Packages #########################################
############################################################################################
import requests
from datetime import datetime
import os
import re

############################################################################################
######################################## Input Data ########################################
############################################################################################

# Request input data
day = 2
base = os.path.dirname(__file__)   # folder where this script lives
path = os.path.join(base, "../session_cookie.txt")
SESSION_COOKIE = open(path).read() # Get session cookie on AOC website. Save locally. Use for authentication
url = f'https://adventofcode.com/2025/day/{day}/input'

# Read puzzle input from cache, or fetch and cache it
year = url.split('/')[3]
day = url.split('/')[-2].replace('day', '')
cache_file = f'{year}d{day}.txt'
if os.path.exists(cache_file):
    input_text = open(cache_file).read().strip()
else:
    headers = {'Cookie': f'session={SESSION_COOKIE}'}
    response = requests.get(url, headers=headers)
    input_text = response.text.strip()
    with open(cache_file, 'w') as f:
        f.write(input_text)

input = input_text.split(',')
current_datetime = datetime.now()

############################################################################################
########################################## Part 1 ##########################################
############################################################################################

# Convert the input to ranges
input = [(int(item.split("-")[0]), int(item.split("-")[1])) for item in input]

# Regex patterns to check for checking two identical halves
PATTERN = re.compile(r'^(\d+)\1$')

# Range title level
def has_leading_zeroes(n: str):
    if n[0] == "0":
        return True
    else:
        return False

# Range child level
def is_eaven_length(n: int):
    n = str(n) # Covert to str for len calc
    if len(n) % 2 == 0:
        return True
    else:
        return False

def is_double_id(n: int):
    n = str(n)
    return PATTERN.fullmatch(n) is not None

invalid_ids = []

for r in input:
    for id in range(r[0], r[1]+1):
        
        # ID of repeated sequence must be of even length
        if not is_eaven_length(id):
            continue
        
        # Check if repeted secuence
        if is_double_id(id):
            invalid_ids.append(id)
        
ans_pt1 = sum(invalid_ids)
print("Answer for part one is: ",ans_pt1)


############################################################################################
########################################## Part 2 ##########################################
############################################################################################    
PATTERN2 = re.compile(r'^(\d+)\1+$')
invalid_ids = []

def is_repeted_id(n: int):
    n = str(n)
    return bool(PATTERN2.fullmatch(str(n)))

for r in input:
    for id in range(r[0], r[1]+1):
        # Check if repeted secuence
        if is_double_id(id):
            invalid_ids.append(id)
        
ans_pt2 = sum(invalid_ids)
print("Answer for part two is: ",ans_pt2)

for i in invalid_ids:
    print(i)
    
    
###### Correct
invalid_ids = []
import re
pat = re.compile(r'^(\d+)\1+$')

def is_repeated_id(s: int) -> bool:
    s = str(s)
    return bool(pat.fullmatch(s))

def repeat_count(s: int) -> int | None:
    s = str(s)
    m = pat.fullmatch(s)
    return len(s) // len(m.group(1)) if m else None

for r in input:
    for id in range(r[0], r[1]+1):
        if is_repeated_id(id):
            invalid_ids.append(id)
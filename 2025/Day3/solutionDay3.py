############################################################################################
######################################### Packages #########################################
############################################################################################
import requests
from datetime import datetime
import os


############################################################################################
######################################## Input Data ########################################
############################################################################################

# Request input data 
# TODO: (Make xentral function!!!)
day = 3
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

lines = input_text.split('\n')
current_datetime = datetime.now()


############################################################################################
########################################## Part 1 ##########################################
############################################################################################


def list_lookup(l: list[int], skip_p: list[int] = None) -> int:
    p = 0
    max_n = 0
    max_p = 0
    for i in l:
        
        # If num in current pos is bigger than current max, assing new max
        # Only if the current position should not be skipped.
        if i>max_n and p not in skip_p:
            max_n = i
            max_p = p
            
        p += 1 # Next position
    return(max_p)


# Loop through each bank and check for the best combination at each block
max_joltage= []
for bank in lines:
    joltage_list = [int(j) for j in bank] # List of joltage ints
    last_pos = len(joltage_list)-1 # Last position in jolatage liste
    
    #First position with highest joltage (skip last position first jilt cannot be in last pos)
    first_pos = list_lookup(joltage_list, [last_pos]) 
    
    #Next position with highest joltage (skip all before first jolt position)
    second_pos = list_lookup(joltage_list, list(range(first_pos+1))) #Second position with highest joltage
    
    joltage = int(str(joltage_list[first_pos]) + str(joltage_list[second_pos]))
    max_joltage.append(joltage)
    
############################################################################################
########################################## Part 2 ##########################################
############################################################################################
"""
Hmm brute force solution where all posible combinations with inherant order is considered,
then the largest out of these 12-digit combinations is considered!
"""

# k = number of batteries to turn on
def max_joltage(bank: list[int], k:int = 2):
    n = len(bank)
    
    if k > n:
        raise ValueError("Number of batteries to turn on (k) cannot be larger than the number of available batteries in the bank")
    
    start_idx = 0
    max_total_jolt = ""
    
    # We need to make sure that there is room for the remaining amount of batteries 
    # (used to decrese end with remaining batteies iteratively)
    for remaining   in range(k,0,-1):
        end = n - remaining
        max_jolt = -1
        max_idx = start_idx
        
        for i in range(start_idx, end+1):
            jolt = bank[i]
            if jolt > max_jolt:
                max_jolt = jolt
                max_idx = i
                if max_jolt == 9: # Cannot find any better
                    break
        max_total_jolt = max_total_jolt + str(max_jolt)
        start_idx = max_idx + 1
    
    return int(max_total_jolt)


# Search through each bank and find its max joltage
max_joltages = []
for bank in lines:
    bank = [int(jolt) for jolt in bank]
    max_jolt = max_joltage(bank=bank, k=12)
    max_joltages.append(max_jolt)
    
sum(max_joltages)
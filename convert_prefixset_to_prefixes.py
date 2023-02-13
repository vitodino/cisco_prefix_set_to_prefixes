# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:57:03 2023

@author: kliunand
"""

import ipaddress

# This function is assuming ge value is never higher than le value

# input type is string. (eg, '172.16.0.0/16 ge 17' or '172.16.0.0/16 le 32', or '172.16.0.0/16 ge 31 le 32', 
# or '172.16.0.0/16 eq 32' or '172.16.0.0/16')
# return list of subnets
def convert_prefixset_entry(entry):
    subnetList = []
    entry_list = entry.strip().split(' ')
    base = entry_list[0].split('/')[0]
    minlen = int(entry_list[0].split('/')[-1])
    midlen = minlen
    maxlen = midlen
    if 'eq' in entry_list:
        midlen = int(entry_list[entry_list.index('eq')+1])
        maxlen = midlen
    elif 'ge' in entry_list and 'le' in entry_list:
        ge = int(entry_list[entry_list.index('ge')+1])
        le = int(entry_list[entry_list.index('le')+1])
        # this is assuming ge value is never higher than le value
        if ge < le or ge == le:
            midlen,maxlen = ge,le
        else:
            raise ValueError('ge value is higher than le value')
    elif 'ge' in entry_list:
        midlen = int(entry_list[entry_list.index('ge')+1])
        maxlen = 32
    elif 'le' in entry_list:
        midlen = minlen
        maxlen = int(entry_list[entry_list.index('le')+1])
    for i in range(midlen,maxlen+1):
        subnetList += list(ipaddress.ip_network(f'{base}/{str(minlen)}').subnets(prefixlen_diff=i-minlen))
    for i in range(len(subnetList)):
        subnetList[i] = str(subnetList[i])
    return subnetList


# input type is string. insert prefix-set configuration as input for below function
# return list of subnets
def convert_prefixset_into_prefixes(prefixset):
    entries = prefixset.split('\n')
    subnetList = []
    for entry in entries:
        if entry.count('.') == 3 and '/' in entry:
            subnetList += convert_prefixset_entry(entry.replace(',',''))
    return subnetList
            
    
    

# if __name__ == '__main__':
#     prefixset = '''prefix-set prefixes
#       172.16.0.0/12 ge 12,
#       192.168.0.0/16 ge 16
#     end-set
#     !'''
#     subnetList = convert_prefixset_into_prefixes(prefixset)
    
        
    

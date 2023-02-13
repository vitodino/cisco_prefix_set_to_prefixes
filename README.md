# cisco_prefix_set_to_prefixes
convert cisco IOS-XR prefix-set policy into a list of prefixes
def convert_prefixset_entry(entry) -> insert a line of prefix-set entry as input (eg, '172.16.0.0/16 ge 17' or '172.16.0.0/16 le 32' or '172.16.0.0/16').
def convert_prefixset_into_prefixes(prefixset) -> insert prefix-set configuration as input:
  (eg.  prefixset = '''prefix-set prefixes
#       10.0.0.0/8 ge 8,
#       172.16.0.0/12 ge 12,
#       192.168.0.0/16 ge 16
#     end-set
#     !''')

both functions return list of subnets/prefixes
